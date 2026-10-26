import unittest
from dataclasses import replace
from research_tools.photon_statistics import (
    PPMCase,poisson,wilson_interval,simulate,ideal_no_background_ser)
from random import Random
from math import exp

class PhotonTests(unittest.TestCase):
    def test_reproducible(self):
        self.assertEqual(simulate(symbols=150,seed=11),simulate(symbols=150,seed=11))
    def test_poisson_zero(self):
        self.assertEqual(poisson(0,Random(9)),0)
    def test_order_validation(self):
        for order in (0,1,3,7):
            with self.assertRaises(ValueError):PPMCase(order=order)
    def test_high_snr(self):
        self.assertLess(simulate(PPMCase(8,12,0),1000,1)["ser"],0.002)
    def test_zero_snr(self):
        p=simulate(PPMCase(8,0,0),10000,1)["ser"]
        self.assertAlmostEqual(p,.875,delta=.02)
    def test_increased_background(self):
        a=simulate(PPMCase(8,2,0),2000,11)["ser"]
        b=simulate(PPMCase(8,2,1.0),2000,11)["ser"]
        self.assertLess(a,b)
    def test_pointing_hurts(self):
        ref=PPMCase(8,2,.08)
        badly=replace(ref,pointing_sigma_rad=ref.gaussian_angular_radius*2)
        self.assertLess(simulate(ref,1800,3)["ser"],simulate(badly,1800,3)["ser"])
    def test_analytic(self):
        self.assertAlmostEqual(ideal_no_background_ser(8,2),.875*exp(-2))
    def test_wilson(self):
        a,b=wilson_interval(0,100);self.assertEqual(a,0);self.assertTrue(0<b<.05)
    def test_reject_large_poisson(self):
        with self.assertRaises(ValueError):poisson(50,Random(1))
if __name__=="__main__":unittest.main()
