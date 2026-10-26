"""Narrowband stellar blackbody photon-background reference model.

A continuum toy model, not a measured Proxima spectrum. The spatial
coupling is an independent assumed factor, not an optical prediction.
Research lead: Biswajit Jana. No FTL claim.
"""
from dataclasses import dataclass
from math import expm1, pi, isfinite

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
LY = 9.4607304725808e15
RSUN = 6.957e8

@dataclass(frozen=True)
class BlackbodyBackground:
    temperature_k: float = 3000.
    star_radius_m: float = .15 * RSUN
    star_distance_m: float = 4.24 * LY
    wavelength_m: float = 1064e-9
    bandpass_m: float = .1e-9
    telescope_diameter_m: float = 10.
    system_efficiency: float = .2
    spatial_coupling: float = 1e-5

    def validate(self):
        for name in ('temperature_k', 'star_radius_m', 'star_distance_m',
                     'wavelength_m', 'bandpass_m', 'telescope_diameter_m'):
            x = getattr(self, name)
            if not isfinite(x) or x <= 0:
                raise ValueError(name)
        for name in ('system_efficiency', 'spatial_coupling'):
            x = getattr(self, name)
            if not isfinite(x) or not 0 <= x <= 1:
                raise ValueError(name)
        if self.star_radius_m >= self.star_distance_m:
            raise ValueError('far-field star required')
        return self

    def stellar_continuum_photons_s(self):
        """Planck B_lambda, unresolved-disk flux, rectangular-band detector rate."""
        self.validate()
        x = H*C/(self.wavelength_m*KB*self.temperature_k)
        B = (2*H*C*C/self.wavelength_m**5)/expm1(x) if x < 700 else 0.
        spectral_irradiance = pi*B*(self.star_radius_m/self.star_distance_m)**2
        collecting_area = pi*(self.telescope_diameter_m/2)**2
        return (collecting_area*spectral_irradiance*self.bandpass_m*
                self.wavelength_m/(H*C)*
                self.system_efficiency*self.spatial_coupling)

    def expected_counts_per_slot(self, slot_s):
        if not isfinite(slot_s) or slot_s <= 0:
            raise ValueError('slot_s')
        return slot_s*self.stellar_continuum_photons_s()

if __name__ == '__main__':
    import json
    from dataclasses import asdict
    x = BlackbodyBackground()
    print(json.dumps({'inputs': asdict(x),
                      'continuum_counts_per_s': x.stellar_continuum_photons_s(),
                      'per_20ms_slot': x.expected_counts_per_slot(.02)}, indent=2))
