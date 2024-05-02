from library import *
from translator import parse_file
import numpy as np
import cv2

# NOTE: To run tests, set variables in translator.py to the following values:
# draw = False
# fileImport = False
# terminalInputs = False


def test_aritmetic():
    """Test grammar for basic aritmetic function"""

    # Get results for file parse
    filename = './test_files/1.aritmetic.txt'
    _, symbols = parse_file(filename)

    # Expected values
    a = 1 + 1 + 5 - 2
    b = a + 2 * (3 + 1)
    c = b * 3 / 4 + (2 + (4 * 3))

    assert a == symbols['a']
    assert b == symbols['b']
    assert c == symbols['c']


def test_numpy():
    """Test grammar for custom numpy functions"""

    # Get results for file parse
    filename = './test_files/2.numpy.txt'
    _, symbols = parse_file(filename)

    # Expected values
    a = 10.5
    b = 34.25
    c = 46.23

    assert np.sum([a,b,c]) == symbols['sum_res']
    assert np.mean([a,b,c]) == symbols['mean_res']
    assert np.max([a,b,c]) == symbols['max_res']
    assert np.min([a,b,c]) == symbols['min_res']
    assert np.median([a,b,c]) == symbols['median_res']
    assert np.std([a,b,c]) == symbols['std_res']
    assert np.sin([a]) == symbols['sin_res']
    assert np.cos([a]) == symbols['cos_res']
    assert np.tan([a]) == symbols['tan_res']


def test_cv2():
    """Test grammar for manage images"""

    # Get results for file parse
    filename = './test_files/3.cv2.txt'
    _, symbols = parse_file(filename)

    # Expected results
    res_gen_matrix = np.array([[1, 2, 3],
                                [4, 5, 6],
                                [7, 8, 9]])
    res_gen_vector = np.array([1,2,3,4,5])
    
    img = cv2.imread('test.jpg') # Test image
    res_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Image in grayscale
    res_canny = cv2.Canny(res_gs, 200, 400) # Canny image
    res_hist = cv2.calcHist([res_gs], [0], None, [256], [0, 256]) # Histogram

    # Save image should create file with the corresponging image at "./test_save.jpg"
    saved_image = cv2.imread('test_save.jpg')
    
    assert np.array_equal(res_gen_matrix, symbols['res_gen_matrix']) # Gen matrix
    assert np.array_equal(res_gen_vector, symbols['res_gen_vector']) # Gen vector
    assert np.array_equal(img, symbols['res_load_image']) # Load image
    assert np.array_equal(res_gs, symbols['res_gs']) # Gray scale
    assert np.array_equal(res_canny, symbols['res_canny']) # Canny
    assert np.array_equal(res_hist, symbols['res_hist']) # Histogram
    assert isinstance(saved_image, np.ndarray) and saved_image.shape == (432, 768, 3) # Save image

test_cv2()