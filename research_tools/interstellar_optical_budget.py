"""Small-aperture far-field optical photon budget and static light-time controls.

No FTL, perfect pointing, ideal circular pupils, no background/atmosphere.
Small receiver relative to the far-field Airy disk; z <= 1e-3.
Research lead: Biswajit Jana.
"""
from dataclasses import dataclass
from math import pi, exp, isfinite
C = 299792458.0
H = 6.62607015e-34
LY = 9.4607304725808e15
JULIAN_YEAR = 365.25*86400.0

@dataclass(frozen=True)
class Link:
    distance_ly: float = 4.24
    wavelength_m: float = 1064e-9
    tx_diameter_m: float = 1.0
    rx_diameter_m: float = 10.0
    transmitted_w: float = 10.0
    end_to_end_efficiency: float = 0.2

    def photon_rate(self):
        vals=(self.distance_ly,self.wavelength_m,self.tx_diameter_m,
              self.rx_diameter_m,self.transmitted_w)
        if any(not isfinite(x) or x <= 0 for x in vals):
            raise ValueError("positive finite distances, wavelength, apertures, power required")
        eta=self.end_to_end_efficiency
        if not isfinite(eta) or not 0<=eta<=1:
            raise ValueError("efficiency must lie in [0,1]")
        R=self.distance_ly*LY
        z=pi*self.tx_diameter_m*self.rx_diameter_m/(2*self.wavelength_m*R)
        if z>1e-3:
            raise ValueError("outside small-receiver far-field approximation")
        capture=z*z/4-z**4/32
        return self.transmitted_w/(H*C/self.wavelength_m)*capture*eta

    def one_way_years(self):
        if not isfinite(self.distance_ly) or self.distance_ly<=0:
            raise ValueError("distance")
        return self.distance_ly*LY/C/JULIAN_YEAR

    def immediate_reply_years(self):
        return 2*self.one_way_years()

def ppm_ser_zero_background(M, mean_signal):
    """Uncoded M-PPM: count photon, else guess among M slots uniformly."""
    if type(M) is not int or M<2 or M&(M-1):
        raise ValueError("M must be a power of two")
    if not isfinite(mean_signal) or mean_signal<0:
        raise ValueError("mean_signal")
    return (1-1/M)*exp(-mean_signal)

if __name__=="__main__":
    import json
    case=Link()
    print(json.dumps({"inputs":case.__dict__, "detected_photons_per_second_ideal":case.photon_rate(),
                      "one_way_light_time_years":case.one_way_years(),
                      "earliest_request_reply_years":case.immediate_reply_years(),
                      "eight_ppm_uncoded_SER_at_one_photon":ppm_ser_zero_background(8,1)},indent=2))
