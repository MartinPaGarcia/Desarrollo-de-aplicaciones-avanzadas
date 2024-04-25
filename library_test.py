from library import *
import numpy as np

def test_my_sum():
    assert my_sum(1, 2, 3) == 6
    assert my_sum(-1, -2, -3) == -6
    assert my_sum(-1, 2, -3) == -2
    assert my_sum(0, 2, 3) == 5

def test_my_mean():
    assert my_mean(1, 2, 3) == 2
    assert my_mean(-1, -2, -3) == -2
    assert my_mean(-1, 2, -3) == -2/3
    assert my_mean(0, 2, 3) == 5/3

def test_my_median():
    assert my_median(1, 2, 3) == 2
    assert my_median(1, 2, 3, 4) == 2.5
    assert my_median(-1, -2, -3) == -2
    assert my_median(-1, 2, -3) == -1

def test_my_std():
    assert np.isclose(my_std(1, 2, 3), np.std([1, 2, 3]))
    assert np.isclose(my_std(-1, -2, -3), np.std([-1, -2, -3]))
    assert np.isclose(my_std(-1, 2, -3), np.std([-1, 2, -3]))

def test_my_max():
    assert my_max(1, 2, 3) == 3
    assert my_max(-1, -2, -3) == -1
    assert my_max(-1, 2, -3) == 2

def test_my_min():
    assert my_min(1, 2, 3) == 1
    assert my_min(-1, -2, -3) == -3
    assert my_min(-1, 2, -3) == -3

def test_my_sin():
    assert np.isclose(my_sin(0), 0)
    assert np.isclose(my_sin(np.pi / 2), 1)
    assert np.isclose(my_sin(-np.pi / 2), -1)

def test_my_cos():
    assert np.isclose(my_cos(0), 1)
    assert np.isclose(my_cos(np.pi), -1)
    assert np.isclose(my_cos(-np.pi), -1)

def test_my_tan():
    assert np.isclose(my_tan(0), 0)
    assert np.isclose(my_tan(np.pi / 4), 1)
    assert np.isclose(my_tan(-np.pi / 4), -1)
