"""Causal-timing-aware framed PPM + soft Viterbi end-to-end experiment.

The accepted bit rate excludes acquisition, interleaving and real terminal
overhead. Perfect slot synchronization is assumed; no CCSDS compliance.
"""
from __future__ import annotations
from dataclasses import dataclass
import json
import numpy as np
from .softppm import bits_to_symbols,simulate_counts,bit_llrs
from .fec import bytes_to_bits,bits_to_bytes,convolutional_encode,viterbi_decode,frame,deframe
from .geometry import C,LY

@dataclass(frozen=True)
class Experiment:
    M:int=8
    pulse_photons:float=8.
    background_photons_per_slot:float=0.08
    slot_width_s:float=0.0001
    seed:int=20261025
    distance_ly:float=4.24

def run(payload:bytes,cfg:Experiment=Experiment()):
    if cfg.slot_width_s<=0 or cfg.distance_ly<0:
        raise ValueError("positive slot duration and nonnegative range required")
    rng=np.random.default_rng(cfg.seed)
    coded=convolutional_encode(bytes_to_bits(frame(payload,sequence=7)))
    bits_per_symbol=cfg.M.bit_length()-1
    pad=(-len(coded))%bits_per_symbol
    padded=np.pad(coded,(0,pad))
    symbols=bits_to_symbols(padded,cfg.M)
    counts=simulate_counts(symbols,cfg.M,cfg.pulse_photons,cfg.background_photons_per_slot,rng)
    llrs=bit_llrs(counts,cfg.pulse_photons,cfg.background_photons_per_slot)[:len(coded)]
    decoded=viterbi_decode(llrs)
    valid=deframe(bits_to_bytes(decoded))==(7,payload)
    duration_s=len(symbols)*cfg.M*cfg.slot_width_s
    light_time_s=cfg.distance_ly*LY/C
    return {
      "seed":cfg.seed,"modulation":"illustrative nonstandard M-PPM","M":cfg.M,
      "signal_photons_per_active_slot":cfg.pulse_photons,
      "background_photons_per_slot":cfg.background_photons_per_slot,
      "symbols":len(symbols),"payload_bytes":len(payload),
      "raw_coded_bit_errors":int(np.count_nonzero((llrs<0).astype(np.uint8)!=coded)),
      "payload_integrity_ok":bool(valid),
      "goodput_bits_s_if_valid":8*len(payload)/duration_s if valid else 0.,
      "transmission_s":duration_s,
      "light_time_s":light_time_s,
      "earliest_complete_reception_s":duration_s+light_time_s,
      "no_pre_lightcone_information":True
    }

def sweep():
    payload=b"New spectral observation, not shared prediction"
    output=[]
    for M in (4,8,16):
        for photons in (0.5,1,2,4,8,12):
            cfg=Experiment(M=M,pulse_photons=photons)
            result=run(payload,cfg)
            output.append({"M":M,"photons":photons,"valid":result["payload_integrity_ok"],
                           "goodput":result["goodput_bits_s_if_valid"]})
    return output

if __name__=="__main__":
    print(json.dumps({"sample":run(b"Hello, Proxima"),"sweep":sweep()},indent=2))
