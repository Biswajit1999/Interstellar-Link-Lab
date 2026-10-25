"""Checks against limiting cases and causal propagation; no observational claim."""
import math
import unittest
from research_tools.modulation import (
    C, LIGHT_YEAR_M, Link, ppm, ook, ppm_ser,
    symmetric_hard_information, trade_study
)


class ModulationTests(unittest.TestCase):
    def test_random_guess_without_signal(self):
        for M in (2, 4, 16, 128):
            self.assertAlmostEqual(ppm_ser(M, 0., .1), 1.-1./M, places=10)

    def test_zero_background_exact_formula(self):
        for M in (2, 8, 64):
            for signal in (.2, 1., 8.):
                self.assertAlmostEqual(ppm_ser(M,signal,0.),
                                       (1.-1./M)*math.exp(-signal),places=11)

    def test_no_message_without_signal(self):
        for M in (2, 16):
            self.assertAlmostEqual(symmetric_hard_information(M,ppm_ser(M,0,2)),
                                   0,places=10)

    def test_perfect_decode_information(self):
        self.assertAlmostEqual(symmetric_hard_information(16,0),4)

    def test_error_monotonic_signal(self):
        self.assertGreater(ppm_ser(16,1.,.05),ppm_ser(16,5.,.05))

    def test_noise_increases_error(self):
        self.assertGreater(ppm_ser(8,3.,.5),ppm_ser(8,3.,0.))

    def test_peak_constraint(self):
        link = Link(100.,5.,.001,1e11,peak_to_average_limit=4)
        self.assertFalse(ppm(16,link)["feasible"])
        self.assertTrue(ppm(4,link)["feasible"])

    def test_no_propagation_shortcut(self):
        link=Link(200.,20.,.002,4.24*LIGHT_YEAR_M)
        for row in trade_study(link):
            self.assertTrue(row["feasible"])
            self.assertGreaterEqual(row["optimistic_complete_message_s"],
                                    row["light_time_s"])
            self.assertAlmostEqual(row["light_time_s"],link.distance_m/C)

    def test_no_ook_signal_no_information(self):
        link=Link(0.,10.,.002,1e10)
        self.assertAlmostEqual(ook(link)["hard_mi_rate_bps"],0.,places=9)

    def test_ook_bright_link(self):
        link=Link(1000.,0.,.005,1e10)
        self.assertGreater(ook(link)["hard_mi_rate_bps"],190.)

    def test_photon_starved_order_not_monotone(self):
        link=Link(200.,20.,.002,1e10)
        self.assertGreater(ppm(8,link)["hard_mi_rate_bps"],
                           ppm(128,link)["hard_mi_rate_bps"])

    def test_bad_inputs_rejected(self):
        for invalid in ((3,1.,0.), (8,-1.,0.), (16,1.,float("nan")),
                        (16,1.,201.)):
            with self.assertRaises(ValueError):
                ppm_ser(*invalid)


if __name__=="__main__":
    unittest.main()
