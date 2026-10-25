"""Photon-counting M-PPM Poisson slot model and soft bit demapper.

For active slot j, count[j] has mean s+b; all other slots have mean b.
LLR is log P(Y|bit=0)/P(Y|bit=1), using log-sum-exp over symbols.
The model assumes exact slot sync and independent photon counts.
"""
from __future__ import annotations
import math
import numpy as np

def _bits(M: int) -> int:
    if type(M) is not int or M < 2 or M & (M-1):
        raise ValueError("M must be a power of two >= 2")
    return M.bit_length()-1

def _lse(arr):
    mx = float(np.max(arr))
    return mx + math.log(float(np.exp(arr-mx).sum())) if mx != -math.inf else -math.inf

def bits_to_symbols(bits, M: int):
    k=_bits(M)
    x=np.asarray(bits,dtype=np.uint8)
    if x.ndim!=1 or len(x)%k or np.any(x>1):
        raise ValueError("binary bits, multiple of log2(M), required")
    return x.reshape(-1,k).dot(1 << np.arange(k-1,-1,-1)).astype(int)

def symbols_to_bits(symbols, M: int):
    k=_bits(M)
    s=np.asarray(symbols)
    if s.ndim!=1 or np.any((s<0)|(s>=M)):
        raise ValueError("invalid symbol indexes")
    return ((s[:,None].astype(int) >> np.arange(k-1,-1,-1)) & 1).astype(np.uint8).ravel()

def simulate_counts(symbols, M, signal, background, rng):
    _bits(M)
    if not all(math.isfinite(a) and a>=0 for a in (signal,background)):
        raise ValueError("photon means must be finite and nonnegative")
    x=np.asarray(symbols,dtype=int)
    if x.ndim!=1 or np.any((x<0)|(x>=M)):
        raise ValueError("invalid symbols")
    means=np.full((len(x),M),background,dtype=float)
    means[np.arange(len(x)),x]+=signal
    return rng.poisson(means)

def bit_llrs(counts, signal, background):
    y=np.asarray(counts)
    if y.ndim!=2 or y.shape[1]<2 or not np.isfinite(y).all() or np.any(y<0) or np.any(y!=np.floor(y)):
        raise ValueError("counts must be nonnegative integers in a two-dimensional matrix")
    n,M=y.shape
    k=_bits(M)
    if not all(math.isfinite(a) and a>=0 for a in (signal,background)):
        raise ValueError("invalid photon means")
    labels=((np.arange(M)[:,None] >> np.arange(k-1,-1,-1))&1).astype(bool)
    out=np.zeros((n,k),dtype=float)
    if signal==0:
        return out.ravel()
    gain=math.log1p(signal/background) if background>0 else None
    for i,row in enumerate(y):
        if background==0:
            detected=np.flatnonzero(row)
            if len(detected)>1:
                raise ValueError("zero-background data contradict the ideal model")
            weights=np.zeros(M)
            if len(detected):
                weights.fill(-math.inf)
                weights[detected[0]]=0.
        else:
            weights=row*gain
        for bit in range(k):
            out[i,bit]=float(np.clip(_lse(weights[~labels[:,bit]])-_lse(weights[labels[:,bit]]),-50,50))
    return out.ravel()

def symbol_information(true_symbols, counts, signal, background):
    """Sample mean of log[p(Y|S)/p(Y)] in bits. Finite-sample bias applies."""
    x=np.asarray(true_symbols)
    y=np.asarray(counts)
    if x.ndim!=1 or y.ndim!=2 or y.shape[0]!=len(x):
        raise ValueError("shape mismatch")
    M=y.shape[1]
    _bits(M)
    if background<=0 or signal<0:
        raise ValueError("requires background > 0 and signal >= 0")
    weights=y*math.log1p(signal/background)
    mx=np.max(weights,axis=1)
    lse=mx+np.log(np.exp(weights-mx[:,None]).sum(axis=1))
    return float(np.mean((math.log(M)+weights[np.arange(len(x)),x]-lse)/math.log(2)))
