"""Reproduce photon-counted coded PPM frame-success and ideal link geometry.

24 parameter points x 60 independent synthetic frames, with Wilson intervals.
The pulse-photon sweep does not constrain equal mean transmitter power.
"""
from __future__ import annotations
from pathlib import Path
import json,math,sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from research_tools.advanced.experiment import Experiment,run
from research_tools.advanced.geometry import OpticalLink,LY,C
ROOT=Path(__file__).resolve().parents[1]

def wilson(k,n,z=1.959963984540054):
    if n<=0:
        raise ValueError("positive independent frame count required")
    p=k/n
    a=1+z*z/n
    mid=(p+z*z/(2*n))/a
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/a
    return max(0.,mid-half),min(1.,mid+half)

def sweep(n=60):
    if n<=0:
        raise ValueError("positive trial count required")
    payload=b"Fresh spectral observation, not forecast."
    result=[]
    for M in (4,8,16):
        for flux in (0.5,1,2,3,4,6,8,12):
            valid=0
            raw=[]
            duration=None
            for trial in range(n):
                cfg=Experiment(M=M,pulse_photons=flux,background_photons_per_slot=.08,
                               slot_width_s=1e-4,
                               seed=20261025+trial*101+M*1000+int(10*flux))
                x=run(payload,cfg)
                valid+=int(x["payload_integrity_ok"])
                raw.append(x["raw_coded_bit_errors"])
                duration=x["transmission_s"]
            result.append({
                "M":M,"signal_photons_per_active_slot":flux,
                "trials":n,"successful_frames":valid,
                "frame_success_rate":valid/n,"wilson_95":wilson(valid,n),
                "mean_raw_coded_errors":float(np.mean(raw)),
                "payload_rate_if_valid_bits_s":8*len(payload)/duration,
            })
    return result

def main():
    records=sweep()
    link=OpticalLink(4.24*LY,1.55e-6,10.,30.,1000.,.2)
    data={
        "date":"2026-10-25",
        "status":"deterministic synthetic trials only",
        "model":"non-CCSDS K=3 convolutional code + soft PPM + independent Poisson detector",
        "slot_seconds":1e-4,
        "background_photons_per_slot":.08,
        "fixed_mean_power_comparison":False,
        "static_reference_range_ly":4.24,
        "light_time_years":4.24,
        "illustrative_optical_case":{"tx_watts":1000,"lambda_nm":1550,"tx_m":10,"rx_m":30,
             "scalar_throughput":.2,"detected_counts_per_s":link.received_photons_per_s()},
        "records":records
    }
    (ROOT/"results").mkdir(parents=True,exist_ok=True)
    (ROOT/"results/optical_modem_v04.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf8")
    fig,ax=plt.subplots(figsize=(9.0,5.0))
    for M in (4,8,16):
        a=[r for r in records if r["M"]==M]
        x=np.array([r["signal_photons_per_active_slot"] for r in a])
        y=np.array([r["frame_success_rate"] for r in a])
        lo=np.array([r["wilson_95"][0] for r in a])
        hi=np.array([r["wilson_95"][1] for r in a])
        ax.plot(x,y,marker="o",label=f"{M}-PPM")
        ax.fill_between(x,lo,hi,alpha=.13)
    ax.set(xlabel="Expected detected photons in active slot",ylabel="CRC-valid frames / 60",
           title="Soft-decision coded PPM: 60 independently seeded frames per operating point")
    ax.set_ylim(-.02,1.02)
    ax.grid(alpha=.25)
    ax.legend()
    fig.tight_layout()
    (ROOT/"figures/engineering").mkdir(parents=True,exist_ok=True)
    fig.savefig(ROOT/"figures/engineering/frame_acceptance_v04.svg")
    fig.savefig(ROOT/"figures/engineering/frame_acceptance_v04.png",dpi=160)
    plt.close(fig)
    print("Records:",len(records),"ideal received photons/s:",round(link.received_photons_per_s(),2))

if __name__=="__main__":
    main()
