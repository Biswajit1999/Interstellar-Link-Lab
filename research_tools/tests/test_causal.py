"""Numerical controls that falsify spurious pre-lightcone interpretations."""
import unittest
from research_tools.causal_controls import (
    C, Event, interval_c2s2, flat_future_causal, binary_mutual_information,
    permutation_p, synthetic_controls
)


class CausalTests(unittest.TestCase):
    def test_null_boundary(self):
        a=Event(0,0)
        b=Event(1.,C)
        self.assertEqual(interval_c2s2(a,b),0.)
        self.assertTrue(flat_future_causal(a,b))

    def test_spacelike(self):
        a=Event(0,0)
        b=Event(.5,C)
        self.assertLess(interval_c2s2(a,b),0.)
        self.assertFalse(flat_future_causal(a,b))

    def test_reverse_timelike_not_future(self):
        self.assertFalse(flat_future_causal(Event(1.,0),Event(0.,0)))

    def test_perfect_message(self):
        x=[0,1]*100
        self.assertAlmostEqual(binary_mutual_information(x,x),1.)

    def test_constant_y_no_information(self):
        x=[0,1]*100
        self.assertAlmostEqual(binary_mutual_information(x,[0]*len(x)),0.)

    def test_reject_nonbinary(self):
        with self.assertRaises(ValueError):
            binary_mutual_information([0,1],[0,2])

    def test_pre_and_late_controls(self):
        rows=synthetic_controls(n=4096,seed=101,draws=199)
        self.assertLess(rows["prearrival_independent"]["empirical_mi_bits"],.01)
        self.assertGreater(rows["postarrival_positive_control"]["empirical_mi_bits"],.8)
        self.assertGreater(rows["intentional_side_channel_positive_control"]["empirical_mi_bits"],.5)
        self.assertLess(rows["postarrival_positive_control"]["permutation_p"],.01)

    def test_permutation_p_is_bounded(self):
        p=permutation_p([0,1]*500,[0,1]*500,draws=19)["permutation_p"]
        self.assertGreaterEqual(p,1./20.)
        self.assertLessEqual(p,1.)


if __name__ == "__main__":
    unittest.main()
