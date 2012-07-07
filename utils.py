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



