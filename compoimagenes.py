#!/usr/bin/env python

"""

Ejemplo simple de composicion de imagenes con opencv.

"""

import os

import cv
import numpy
from utils import cv2array

foreground = cv.LoadImage(os.path.join('data', 'wallpaper.png'), 1)
foreground = cv2array(foreground) / 255.0
mask = cv.LoadImage(os.path.join('data', 'mask.png'), 1)
mask = cv2array(mask) / 255.0
background = cv.LoadImage(os.path.join('data', 'background.png'), 1)
background = cv2array(background) / 255.0


def show_video():
    result = foreground * mask + background * (1 - mask)
    cv.ShowImage('Video', cv.fromarray(result))


cv.NamedWindow('Video')


exit = False
while not exit:
    show_video()
    # if scape is pressed:
    if cv.WaitKey(10) == 27:
        exit = True
