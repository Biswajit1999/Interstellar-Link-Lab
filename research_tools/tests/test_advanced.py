"""Regression controls for the simplified Photon Frontier modem."""
import math
import unittest
import numpy as np
from research_tools.advanced.softppm import bits_to_symbols,symbols_to_bits,simulate_counts,bit_llrs,symbol_information
from research_tools.advanced.fec import bytes_to_bits,bits_to_bytes,convolutional_encode,viterbi_decode,frame,deframe
from research_tools.advanced.geometry import moving_light_time,point_ahead_angle_rad,OpticalLink,C,LY
from research_tools.advanced.gr_benchmarks import shapiro_delay_s,SUN_MASS_KG,AU_M
from research_tools.advanced.experiment import run,Experiment

class ModemTests(unittest.TestCase):
    def test_frame_crc(self):
        b=frame(b"fresh message",7)
        self.assertEqual(deframe(b),(7,b"fresh message"))
        a=bytearray(b);a[-5]^=1
        self.assertIsNone(deframe(bytes(a)))
    def test_code_noiseless(self):
        b=bytes_to_bits(b"measured feature 42")
        code=convolutional_encode(b)
        llr=np.where(code==0,9.,-9.)
        self.assertTrue(np.array_equal(viterbi_decode(llr),b))
        llr[18:20]*=-1
        self.assertTrue(np.array_equal(viterbi_decode(llr),b))
    def test_ppm_bits(self):
        for M in (2,4,8,16):
            k=M.bit_length()-1
            b=np.tile([0,1,1,0],6).astype(np.uint8)
            b=b[:len(b)//k*k]
            self.assertTrue(np.array_equal(symbols_to_bits(bits_to_symbols(b,M),M),b))
    def test_count_llrs(self):
        rng=np.random.default_rng(10)
        bits=np.tile([0,1,1,0],20).astype(np.uint8)
        counts=simulate_counts(bits_to_symbols(bits,4),4,40,0,rng)
        self.assertTrue(np.array_equal((bit_llrs(counts,40,0)<0).astype(np.uint8),bits))
    def test_zero_information(self):
        rng=np.random.default_rng(10)
        x=rng.integers(0,8,size=200)
        y=simulate_counts(x,8,0,0.3,rng)
        self.assertAlmostEqual(symbol_information(x,y,0,0.3),0,places=11)
    def test_invalid(self):
        self.assertRaises(ValueError,bits_to_symbols,np.array([2,0]),4)
        self.assertRaises(ValueError,simulate_counts,np.array([0]),3,2,0.1,np.random.default_rng(1))
        self.assertRaises(ValueError,bit_llrs,np.array([[1,-1],[0,1]]),1,0.1)
        self.assertRaises(ValueError,bits_to_bytes,np.array([1,1,0]))
    def test_high_flux_frame(self):
        x=run(b"fresh photons",Experiment(M=8,pulse_photons=12))
        self.assertTrue(x["payload_integrity_ok"])
        self.assertGreater(x["earliest_complete_reception_s"],x["light_time_s"])
    def test_no_signal(self):
        x=run(b"fresh photons",Experiment(M=8,pulse_photons=0))
        self.assertFalse(x["payload_integrity_ok"])
        self.assertEqual(x["goodput_bits_s_if_valid"],0)

class GeometryTests(unittest.TestCase):
    def test_static(self):
        self.assertAlmostEqual(moving_light_time([LY,0,0],[0,0,0]),LY/C)
    def test_radial(self):
        d=1.e11;v=20000.
        self.assertAlmostEqual(moving_light_time([d,0,0],[v,0,0]),d/(C-v),places=7)
    def test_transverse(self):
        self.assertAlmostEqual(point_ahead_angle_rad([1e11,0,0],[0,30000,0]),30000/C,delta=2e-8)
    def test_invalid(self):
        self.assertRaises(ValueError,moving_light_time,[1e10,0,0],[C,0,0])
    def test_optical(self):
        o=OpticalLink(4.24*LY,1.55e-6,10.,30.,1000.,0.2)
        self.assertTrue(0<o.airy_encircled_fraction()<1)
        self.assertGreater(o.received_photons_per_s(),0)
    def test_shapiro(self):
        self.assertEqual(shapiro_delay_s(0,AU_M,AU_M,AU_M),0)
        self.assertTrue(0<shapiro_delay_s(SUN_MASS_KG,AU_M,AU_M,AU_M)<0.001)

if __name__=="__main__":
    unittest.main()
