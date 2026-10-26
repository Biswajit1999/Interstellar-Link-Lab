"""Analytical scaling controls for the illustrative blackbody continuum."""
from dataclasses import replace
import unittest
from research_tools.advanced.stellar_background import BlackbodyBackground

class BlackbodyModelTests(unittest.TestCase):
    def setUp(self): self.x = BlackbodyBackground()
    def test_baseline(self):
        self.assertAlmostEqual(self.x.stellar_continuum_photons_s(),1.74203031654,places=8)
    def test_zero_coupling(self):
        self.assertEqual(replace(self.x,spatial_coupling=0).stellar_continuum_photons_s(),0)
    def test_aperture_square(self):
        y=replace(self.x,telescope_diameter_m=20).stellar_continuum_photons_s()
        self.assertAlmostEqual(y/self.x.stellar_continuum_photons_s(),4)
    def test_distance_inverse_square(self):
        y=replace(self.x,star_distance_m=2*self.x.star_distance_m).stellar_continuum_photons_s()
        self.assertAlmostEqual(y/self.x.stellar_continuum_photons_s(),.25)
    def test_bandwidth(self):
        y=replace(self.x,bandpass_m=.2e-9).stellar_continuum_photons_s()
        self.assertAlmostEqual(y/self.x.stellar_continuum_photons_s(),2)
    def test_invalid(self):
        with self.assertRaises(ValueError):
            replace(self.x,temperature_k=0).stellar_continuum_photons_s()
        with self.assertRaises(ValueError):
            replace(self.x,spatial_coupling=1.1).stellar_continuum_photons_s()
    def test_slot_scaling(self):
        self.assertAlmostEqual(self.x.expected_counts_per_slot(.04)/
                               self.x.expected_counts_per_slot(.02),2)
if __name__=='__main__': unittest.main()
