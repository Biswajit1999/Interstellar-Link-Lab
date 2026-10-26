"""Regression controls for analytical interstellar far-field envelope."""
import unittest
from dataclasses import replace
from math import exp
from research_tools.interstellar_optical_budget import Link,ppm_ser_zero_background

class OpticalBudgetTests(unittest.TestCase):
    def test_photon_rate_baseline(self):
        self.assertAlmostEqual(Link().photon_rate(),0.362752442112,places=7)
    def test_power_linear(self):
        self.assertAlmostEqual(replace(Link(),transmitted_w=20).photon_rate()/Link().photon_rate(),2)
    def test_inverse_square_distance(self):
        self.assertAlmostEqual(Link().photon_rate()/replace(Link(),distance_ly=8.48).photon_rate(),4)
    def test_aperture_square(self):
        self.assertAlmostEqual(replace(Link(),tx_diameter_m=2).photon_rate()/Link().photon_rate(),4)
    def test_zero_efficiency(self):
        self.assertEqual(replace(Link(),end_to_end_efficiency=0).photon_rate(),0)
    def test_reject_nonphysical(self):
        for bad in (Link(transmitted_w=0),Link(rx_diameter_m=-1),Link(end_to_end_efficiency=2)):
            with self.assertRaises(ValueError):bad.photon_rate()
    def test_lighttime(self):
        self.assertAlmostEqual(Link().one_way_years(),4.24)
        self.assertAlmostEqual(Link().immediate_reply_years(),8.48)
    def test_ppm_null(self):
        self.assertAlmostEqual(ppm_ser_zero_background(8,0),7/8)
        self.assertAlmostEqual(ppm_ser_zero_background(8,2),7*exp(-2)/8)
    def test_invalid_M(self):
        with self.assertRaises(ValueError):ppm_ser_zero_background(3,1)

if __name__=="__main__":unittest.main()
