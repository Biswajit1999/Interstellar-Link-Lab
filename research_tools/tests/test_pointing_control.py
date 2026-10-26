import unittest
from dataclasses import replace
from research_tools.pointing_control import Control,run

class SteeringTests(unittest.TestCase):
    def test_reproducible(self):
        cfg=Control(steps=600,warmup_steps=100)
        self.assertEqual(run(cfg,3),run(cfg,3))
    def test_closed_loop_reduces_error(self):
        r=run()
        self.assertLess(r["closed_rms_rad"],r["open_rms_rad"]*.5)
        self.assertGreater(r["avg_closed_gaussian_overlap"],r["avg_open_gaussian_overlap"])
    def test_zero_noise(self):
        r=run(Control(disturbance_drive_sigma_rad=0,measurement_sigma_rad=0,steps=500,warmup_steps=50))
        self.assertEqual(r["open_rms_rad"],0)
        self.assertEqual(r["closed_rms_rad"],0)
        self.assertEqual(r["avg_closed_gaussian_overlap"],1.)
    def test_bad_parameters(self):
        with self.assertRaises(ValueError): Control(dt_s=0)
        with self.assertRaises(ValueError): Control(steps=50)
        with self.assertRaises(ValueError): Control(disturbance_memory=1)
    def test_saturation_limit(self):
        r=run(Control(stroke_rad=1e-7,steps=500,warmup_steps=100))
        self.assertLess(r["avg_closed_gaussian_overlap"],1.01)
if __name__=="__main__":unittest.main()
