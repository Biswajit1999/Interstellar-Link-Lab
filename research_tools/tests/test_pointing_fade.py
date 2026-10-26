"""Independent regressions for packet-correlated pointing and Poisson PPM."""
import unittest
from dataclasses import replace
from math import exp
from random import Random
from research_tools.pointing_fade import (
    GaussianOpticalTerminal, zero_background_ppm_ser,
    uncoded_packet_success, correlated_packet_success,
    monte_carlo_correlated_packet, zero_background_soft_information, study
)

class GaussianOptics(unittest.TestCase):
    def setUp(self):
        self.t=GaussianOpticalTerminal()

    def test_farfield_scaling(self):
        t=self.t
        self.assertAlmostEqual(t.beam_radius_m()/t.distance_m/t.divergence_rad_farfield(),1,places=10)

    def test_jitter_gain_against_random_samples(self):
        t=replace(self.t,pointing_sigma_axis_rad=.6e-6)
        rng=Random(7)
        measured=sum(t.draw_gain(rng) for _ in range(30000))/30000
        self.assertAlmostEqual(measured,t.mean_fade_gain(),delta=.012)

    def test_outage_against_random_samples(self):
        t=replace(self.t,pointing_sigma_axis_rad=.5e-6)
        rng=Random(9)
        measured=sum(t.draw_gain(rng)<.5 for _ in range(30000))/30000
        self.assertAlmostEqual(measured,t.outage(.5),delta=.014)

    def test_zero_jitter_exact(self):
        self.assertEqual(self.t.mean_fade_gain(),1)
        self.assertEqual(self.t.outage(.5),0)
        self.assertEqual(self.t.draw_gain(Random(9)),1)

    def test_power_linearity(self):
        t=replace(self.t,transmit_average_power_w=20)
        self.assertAlmostEqual(t.photons_mean_per_s()/self.t.photons_mean_per_s(),2)

    def test_inverse_square_farfield(self):
        t=replace(self.t,distance_m=2*self.t.distance_m)
        self.assertAlmostEqual(self.t.photons_mean_per_s()/t.photons_mean_per_s(),4,places=9)

    def test_small_receiver_capture_limit(self):
        t=replace(self.t,pointing_sigma_axis_rad=.5e-6)
        self.assertAlmostEqual(t.mean_capture_exact_gaussian()/
            (t.on_axis_capture_small()*t.mean_fade_gain()),1,places=10)

    def test_pointing_reduces_photon_rate(self):
        self.assertLess(replace(self.t,pointing_sigma_axis_rad=1e-6).photons_mean_per_s(),
                        self.t.photons_mean_per_s())

    def test_reject_bad_physics(self):
        for t in [replace(self.t,tx_waist_radius_m=0),
                  replace(self.t,pointing_sigma_axis_rad=-1),
                  replace(self.t,end_to_end_efficiency=1.1),
                  replace(self.t,rx_aperture_radius_m=1e15)]:
            with self.assertRaises(ValueError):t.photons_mean_per_s()

    def test_invalid_outage_threshold(self):
        with self.assertRaises(ValueError):self.t.outage(0)

class PhotonInformation(unittest.TestCase):
    def test_empty_signal(self):
        self.assertAlmostEqual(zero_background_ppm_ser(8,0),.875)
        self.assertEqual(zero_background_soft_information(8,0),0)

    def test_symbol_error_closed_form(self):
        self.assertAlmostEqual(zero_background_ppm_ser(8,2),.875*exp(-2))

    def test_soft_information_closed_form(self):
        self.assertAlmostEqual(zero_background_soft_information(8,1),3*(1-exp(-1)))

    def test_information_bound(self):
        for s in (.01,1.,8.):
            self.assertLessEqual(zero_background_soft_information(16,s),4)

    def test_independent_conditional_symbols(self):
        p=uncoded_packet_success(8,2,1)
        self.assertAlmostEqual(uncoded_packet_success(8,2,16),p**16)

    def test_zero_jitter_matches_conditional(self):
        t=GaussianOpticalTerminal()
        self.assertAlmostEqual(correlated_packet_success(8,2,16,t),
                               uncoded_packet_success(8,2,16))

    def test_integrated_fade_against_mc(self):
        t=replace(GaussianOpticalTerminal(),pointing_sigma_axis_rad=.5e-6)
        exact=correlated_packet_success(8,2,12,t)
        mc=monte_carlo_correlated_packet(8,2,12,t,n=30000,seed=8)
        self.assertAlmostEqual(exact,mc["expected_success"],delta=5*mc["standard_error"]+.004)

    def test_mean_power_can_miss_packet_loss(self):
        t=replace(GaussianOpticalTerminal(),pointing_sigma_axis_rad=1e-6)
        s=t.photons_on_axis_per_s()*100
        self.assertLess(correlated_packet_success(8,s,16,t),.4)
        self.assertGreater(uncoded_packet_success(8,s*t.mean_fade_gain(),16),.98)

    def test_invalid_modulation_and_quadrature(self):
        with self.assertRaises(ValueError):zero_background_ppm_ser(3,1)
        with self.assertRaises(ValueError):
            correlated_packet_success(8,2,2,GaussianOpticalTerminal(),steps=5)

    def test_study_has_six_cases(self):
        self.assertEqual(len(study()["rows"]),6)

if __name__=="__main__":
    unittest.main()
