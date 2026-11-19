import numpy as np
import pytest
from research_tools.endpoint_audit_20261119 import C, intercept_time, point_ahead, finite_difference_time_gradient

def test_static():
    assert np.isclose(intercept_time([C*10,0,0],[0,0,0]),10)

def test_receding():
    assert np.isclose(intercept_time([C*10,0,0],[0.1*C,0,0]),10/0.9)

def test_approaching():
    assert np.isclose(intercept_time([C*10,0,0],[-0.1*C,0,0]),10/1.1)

def test_transverse_point_ahead():
    t,d,a = point_ahead([C*10,0,0],[0,0.1*C,0])
    assert np.isclose(a,np.arcsin(0.1))
    assert np.isclose(np.linalg.norm(d),1)

def test_gradient():
    g = finite_difference_time_gradient([C*10,0,0],[0,0,0])
    assert np.isclose(g[0],1/C,rtol=1e-5)

def test_superluminal_rejected():
    with pytest.raises(ValueError):
        intercept_time([1,0,0],[C,0,0])
