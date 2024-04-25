import numpy as np
import cv2
import matplotlib.pyplot as plt

def load_image(path):
    path = path.strip()
    return cv2.imread(path)

def save_image(filename, image):
    cv2.imwrite(filename, image)

def show_image(img):
    cv2.imshow('window' , img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img

def search_cv2(function_name):
    try:
        return getattr(cv2, function_name)
    except Exception as e:
        return "AttributeError: module 'cv2' has no attribute", e

def gen_matrix(a, b, *args):
    s = np.array(args)
    return s.reshape(int(a), int(b))

def gen_vector(*args):
    s =  np.array(args)
    return s

def gray_scale(img):
    img = load_image(img)
    gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gs

def histogram(img):
    '''
        IMPORTANT NOTICE: FOR THIS CODE SNIPPET WE BASED OURSELVES ON THE OFFICIAL OPEN CV DOCUMENTATION
        SPECIFICALLY IN THE FOLLOWING LINK: https://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html
        AND WE ADAPTED IT TO OUR CODE TO AUTOMATE THE PROCESS OF OBTAINING HISTOGRAMS OF IMAGES
    '''
    img = gray_scale(img)
    hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist_full)
    plt.show()

def canny_edge(img):
    '''
        IMPORTANT NOTICE: FOR THIS CODE SNIPPET WE BASED OURSELVES ON THE OFFICIAL OPEN CV DOCUMENTATION
        SPECIFICALLY IN THE FOLLOWING LINK: https://docs.opencv.org/4.x/da/d22/tutorial_py_canny.html
        AND WE ADAPTED IT TO OUR CODE TO AUTOMATE THE PROCESS OF EDGE DETECTION
    '''
    img = gray_scale(img)
    edges = cv2.Canny(img,200,400)
    
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    
    plt.show()

def my_sum(*args):
    s =  np.array(args)
    return np.sum(s)

def my_mean(*args):
    s =  np.array(args)
    return np.mean(s)

def my_median(*args):
    s =  np.array(args)
    return np.median(s)

def my_std(*args):
    s =  np.array(args)
    return np.std(s)

def my_max(*args):
    s =  np.array(args)
    return np.max(s)

def my_min(*args):
    s =  np.array(args)
    return np.min(s)

def my_sin(*args):
    s =  np.array(args)
    return np.sin(s)

def my_cos(*args):
    s =  np.array(args)
    return np.cos(s)

def my_tan(*args):
    s =  np.array(args)
    return np.tan(s)
