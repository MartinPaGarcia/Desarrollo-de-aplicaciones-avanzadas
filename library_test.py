from library import *
import numpy as np 

def test_my_sum():
    assert my_sum(1, 2, 3) == 6

def test_my_mean():
    assert my_mean(1, 2, 3) == 2

def test_my_median():
    assert my_median(1, 2, 3) == 2

def test_my_std():
    assert np.isclose(my_std(1, 2, 3), np.std([1, 2, 3]))

def test_my_max():
    assert my_max(1, 2, 3) == 3

def test_my_min():
    assert my_min(1, 2, 3) == 1

def test_my_sin():
    assert np.isclose(my_sin(np.pi / 2), 1)

def test_my_cos():
    assert np.isclose(my_cos(0), 1)

def test_my_tan():
    assert np.isclose(my_tan(0), 0)