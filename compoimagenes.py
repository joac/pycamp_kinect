#!/usr/bin/env python

"""

Ejemplo simple de composicion de imagenes con opencv.

"""

import os

import cv
import numpy
from utils import load_image_as_array


foreground = load_image_as_array('wallpaper.png')
mask = load_image_as_array('mask.png')
background = load_image_as_array('background.png')


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
