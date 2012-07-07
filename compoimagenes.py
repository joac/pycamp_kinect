#!/usr/bin/env python

"""

Ejemplo simple de composicion de imagenes con opencv.

"""

import os

import cv
import numpy
from scipy import misc

foreground = misc.imread(os.path.join('data', 'wallpaper.png')) / 255.0
mask = misc.imread(os.path.join('data', 'mask.png')) / 255.0
background = misc.imread(os.path.join('data', 'background.png')) / 255.0


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
