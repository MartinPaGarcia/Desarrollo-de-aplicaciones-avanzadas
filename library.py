import numpy as np
import matplotlib as plt
import cv2

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