import numpy as np
import matplotlib
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
    return None

def gen_matrix(a, b, *args):
    s = np.array(args)
    return s.reshape(int(a), int(b))

def gen_vector(*args):
    s =  np.array(args)
    return s

def multiplot_show(nrows, ncols, *args):
    
    if( type(nrows) is float):
        nrows = int(nrows)
    if( type(ncols) is float):
        ncols = int(ncols)
        
    
    args_i = 0
    for i in range(1,nrows+1):
        for j in range(1,ncols+1):
            if(args_i < len(args)):
                # print(f"going for r:{i} c:{j} idx:{args_i+1}")
                plt.subplot(nrows,ncols,args_i+1)
                red = args[args_i][:,:,2].copy()
                args[args_i][:,:,2] = args[args_i][:,:,0] 
                args[args_i][:,:,0] = red
                
                plt.imshow(args[args_i] )
                plt.title(f'img_{args_i}')
                args_i += 1
    
    
    plt.show()
    plt.close()


def histogram(img):
    '''
        NOTA IMPORTANTE: PARA ESTA PORCIÓN DE CÓDIGO NOS BASAMOS EN LA DOCUMENTACIÓN OFICIAL DE OPEN CV
        ESPECÍFICAMENTE EN EL SIGUIENTE ENLACE: https://docs.opencv.org/4.x/d1/db7/tutorial_py_histogram_begins.html
        Y LO ADAPTAMOS A NUESTRO CÓDIGO PARA AUTOMATIZAR EL PROCESO DE OBTENCIÓN DE HISTOGRAMAS DE IMÁGENES
    '''
    load_image(img)
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    hist_full = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(hist_full)
    plt.show()

# ---------------- Funciones matemáticas de numpy ----------------

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