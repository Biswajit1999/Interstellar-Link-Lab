import math
import unittest
from research_tools.relativistic_geometry import (
    C,LY,JULIAN_YEAR,Endpoint,travel,round_trip,intercept_delay,
    point_ahead_angle,position_uncertainty_mc)

class GeometryTests(unittest.TestCase):
    def setUp(self):
        self.a=Endpoint((0.,0.,0.),(0.,0.,0.))
        self.b=Endpoint((4.24*LY,0.,0.),(0.,0.,0.))

    def test_static_ly(self):
        self.assertAlmostEqual(travel(self.a,self.b)["delay_s"]/JULIAN_YEAR,4.24)
    def test_round_trip(self):
        self.assertAlmostEqual(round_trip(self.a,self.b)["total_s"]/JULIAN_YEAR,8.48)
    def test_processing(self):
        r=round_trip(self.a,self.b,processing_s=7)
        self.assertAlmostEqual(r["total_s"],8.48*JULIAN_YEAR+7,places=2)
    def test_radial_receding(self):
        b=Endpoint((C*10,0.,0.),(C*0.1,0.,0.))
        self.assertAlmostEqual(travel(self.a,b)["delay_s"],10/.9)
    def test_radial_approaching(self):
        b=Endpoint((C*10,0.,0.),(-C*0.1,0.,0.))
        self.assertAlmostEqual(travel(self.a,b)["delay_s"],10/1.1)
    def test_point_ahead_static(self):
        self.assertLess(point_ahead_angle(self.a,self.b),1e-6)
    def test_point_ahead_transverse(self):
        b=Endpoint((LY,0.,0.),(0.,20000.,0.))
        self.assertAlmostEqual(point_ahead_angle(self.a,b),math.asin(20000/C),places=5)
    def test_uncertainty_reproducible(self):
        x=position_uncertainty_mc(self.a,self.b,1000.,0.,32,7)
        self.assertEqual(x,position_uncertainty_mc(self.a,self.b,1000.,0.,32,7))
    def test_uncertainty_zero(self):
        x=position_uncertainty_mc(self.a,self.b,0.,0.,16)
        self.assertAlmostEqual(x["mean_s"],4.24*JULIAN_YEAR)
        self.assertAlmostEqual(x["std_s"],0.)
    def test_superluminal_rejected(self):
        with self.assertRaises(ValueError):Endpoint((0.,0.,0.),(C,0.,0.))
    def test_negative_processing_rejected(self):
        with self.assertRaises(ValueError):round_trip(self.a,self.b,processing_s=-1)
if __name__=="__main__":unittest.main()
