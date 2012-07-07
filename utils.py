import cv
import numpy as np
from scipy import ndimage, misc

ones = np.ones((480, 640, 3))
background = misc.imread('data/wallpaper.png')
background = background / 255.0

def alpha_blend(image):

    image, alpha = np.dsplit(image, np.array([3]))
    image = image / 255.0
    alpha = 1 - alpha / 255.0
    alpha = np.dstack((alpha, alpha, alpha))

    resultado = image * alpha + background * (ones - alpha)
    return resultado


_cached = None


def process_depth(depth):
    global _cached

    current = depth / 2047.0
#    current = depth.astype(np.uint8)

    if _cached is not None:
        promedio = (_cached + current) / 2.0
        current = promedio 
    _cached = current

    current *= 255
    current = depth.astype(np.uint8)

    return current

def countours_detection(img):
    """Detectar los bordes de la imagen"""
    a = cv.FindContours(img, cv.CreateMemStorage())
    cv.DrawContours(img, a, cv.RGB(122, 122,12), cv.RGB(17, 110, 2), 40)

def cv2array(im):
    depth2dtype = {
        cv.IPL_DEPTH_8U: 'uint8',
        cv.IPL_DEPTH_8S: 'int8',
        cv.IPL_DEPTH_16U: 'uint16',
        cv.IPL_DEPTH_16S: 'int16',
        cv.IPL_DEPTH_32S: 'int32',
        cv.IPL_DEPTH_32F: 'float32',
        cv.IPL_DEPTH_64F: 'float64',
    }

    arrdtype = im.depth
    a = np.fromstring(im.tostring(), dtype=depth2dtype[im.depth],
                      count=im.width * im.height * im.nChannels)
    a.shape = (im.height, im.width, im.nChannels)
    return a


def array2cv(a):
    dtype2depth = {
        'uint8':   cv.IPL_DEPTH_8U,
        'int8':    cv.IPL_DEPTH_8S,
        'uint16':  cv.IPL_DEPTH_16U,
        'int16':   cv.IPL_DEPTH_16S,
        'int32':   cv.IPL_DEPTH_32S,
        'float32': cv.IPL_DEPTH_32F,
        'float64': cv.IPL_DEPTH_64F,
    }
    try:
        nChannels = a.shape[2]
    except:
        nChannels = 1
    cv_im = cv.CreateImageHeader((a.shape[1], a.shape[0]),
                                 dtype2depth[str(a.dtype)],
                                 nChannels)
    cv.SetData(cv_im, a.tostring(), a.dtype.itemsize * nChannels * a.shape[1])
    return cv_im
