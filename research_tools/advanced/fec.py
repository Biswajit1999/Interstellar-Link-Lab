"""Framing, CRC, educational convolutional coding and soft Viterbi decoding.

Constraint length K=3, rate 1/2, (7,5) octal generators; not a CCSDS codec.
"""
from __future__ import annotations
import struct
import zlib
import numpy as np

def bytes_to_bits(data: bytes):
    return np.unpackbits(np.frombuffer(data,dtype=np.uint8),bitorder="big")

def bits_to_bytes(bits):
    x=np.asarray(bits,dtype=np.uint8)
    if x.ndim!=1 or len(x)%8 or np.any(x>1):
        raise ValueError("binary, byte-aligned array required")
    return np.packbits(x,bitorder="big").tobytes()

def _outputs(state,bit):
    previous=(state>>1)&1
    older=state&1
    return (bit^previous^older,bit^older)

def convolutional_encode(data):
    x=np.asarray(data,dtype=np.uint8)
    if x.ndim!=1 or np.any(x>1):
        raise ValueError("binary vector required")
    out=np.empty(2*(len(x)+2),dtype=np.uint8)
    state=0
    for i,bit in enumerate([*x.tolist(),0,0]):
        out[2*i:2*i+2]=_outputs(state,bit)
        state=(bit<<1)|(state>>1)
    return out

def viterbi_decode(llrs):
    """Max-log soft decode of ln P(Y|0)/P(Y|1). Hard terminated to state zero."""
    obs=np.asarray(llrs,dtype=float)
    if obs.ndim!=1 or len(obs)<4 or len(obs)%2 or not np.isfinite(obs).all():
        raise ValueError("finite, even-length LLR vector required")
    n=len(obs)//2
    metric=np.full(4,np.inf)
    metric[0]=0.
    parent=np.zeros((n,4),dtype=np.uint8)
    symbol=np.zeros((n,4),dtype=np.uint8)
    for t in range(n):
        nxt=np.full(4,np.inf)
        for state in range(4):
            if not np.isfinite(metric[state]):
                continue
            for bit in (0,1):
                target=(bit<<1)|(state>>1)
                a,b=_outputs(state,bit)
                cost=metric[state]+0.5*((2*a-1)*obs[2*t]+(2*b-1)*obs[2*t+1])
                if cost<nxt[target]:
                    nxt[target]=cost
                    parent[t,target]=state
                    symbol[t,target]=bit
        metric=nxt-np.min(nxt)
    state=0
    data=np.empty(n,dtype=np.uint8)
    for t in range(n-1,-1,-1):
        data[t]=symbol[t,state]
        state=int(parent[t,state])
    return data[:-2]

def frame(payload: bytes,sequence: int=0) -> bytes:
    if not isinstance(payload,bytes) or len(payload)>65535 or not 0<=sequence<=65535:
        raise ValueError("invalid frame data")
    body=struct.pack(">HH",sequence,len(payload))+payload
    return body+struct.pack(">I",zlib.crc32(body)&0xffffffff)

def deframe(data: bytes):
    if len(data)<8:
        return None
    sequence,n=struct.unpack(">HH",data[:4])
    if len(data)!=n+8:
        return None
    checksum=struct.unpack(">I",data[-4:])[0]
    if zlib.crc32(data[:-4])&0xffffffff!=checksum:
        return None
    return sequence,data[4:-4]
