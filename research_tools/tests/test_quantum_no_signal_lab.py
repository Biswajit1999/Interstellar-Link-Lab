import math
import unittest
from research_tools.quantum_no_signal_lab import (
    bell_joint, bob_marginal, information_bits, experiment,
)


class BellControl(unittest.TestCase):
    def test_normalized_joint(self):
        for a in (0.0, .2, 1.0, math.pi/2):
            for b in (0.0, .5, math.pi/2):
                self.assertAlmostEqual(sum(bell_joint(i,j,a,b)
                    for i in (0,1) for j in (0,1)),1.,places=12)

    def test_no_local_signal_for_any_alice_basis(self):
        for a in (0, math.pi/12, math.pi/4, math.pi/2, math.pi):
            self.assertAlmostEqual(bob_marginal(a)[0],.5,places=12)
            self.assertAlmostEqual(bob_marginal(a)[1],.5,places=12)

    def test_matched_basis_correlations(self):
        for a in (0,math.pi/2):
            self.assertAlmostEqual(bell_joint(0,1,a,a),0.,places=12)

    def test_orthogonal_basis_independence(self):
        for i in (0,1):
            for j in (0,1):
                self.assertAlmostEqual(bell_joint(i,j,math.pi/2,0),.25,places=12)

    def test_reproducible_sampling(self):
        self.assertEqual(experiment(1000,3,False,19),experiment(1000,3,False,19))

    def test_null_has_no_meaningful_leakage(self):
        s=experiment(6000,23,False,29)
        self.assertLess(s["empirical_setting_to_Bob_MI_bits"],.01)

    def test_positive_control_is_detected(self):
        s=experiment(6000,23,True,29)
        self.assertGreater(s["empirical_setting_to_Bob_MI_bits"],.02)
        self.assertLessEqual(s["iid_permutation_p"],1/30+1e-12)

    def test_rejects_bad_inputs(self):
        with self.assertRaises(ValueError): bell_joint(4,0,0,0)
        with self.assertRaises(ValueError): experiment(0)
        with self.assertRaises(ValueError): information_bits([0],[0,1])


if __name__=="__main__": unittest.main()
