#!/usr/bin/env python
import freenect
import cv
import frame_convert
import numpy as np
#from utils import alpha_blend, process_depth, alpha_from_depth, load_image_as_array

threshold =11
current_depth = 0
depth = None

from utils import *



background = load_image_as_array('wallpaper.png')

def change_threshold(value):
    global threshold
    threshold = value + 1


def change_depth(value):
    global current_dept
    current_depth = value + 1


def show_depth():
    global threshold
    global current_depth
    global depth

    depth, timestamp = freenect.sync_get_depth()

    depth = process_depth(depth, threshold, current_depth)

    #depth = np.logical_and(depth >= current_depth - threshold,
    #                             depth <= current_depth + threshold)

    image = array2cv(depth)

    cv.ShowImage('Depth', image)


def show_video():
    video = freenect.sync_get_video()[0]
    bgr = frame_convert.video_cv(video)
    video = video / 255.00
    bgra = bgra_from_depth(video, depth) 

    rgb = alpha_blend(bgra, background)
    rgb = cv.fromarray(rgb)

    cv.ShowImage('Video', rgb)



cv.NamedWindow('Depth')
cv.NamedWindow('Video')
cv.CreateTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)
cv.CreateTrackbar('depth',     'Depth', current_depth, 2048, change_depth)

print('Press ESC in window to stop')

if __name__ == '__main__':
    while 1:
        show_depth()
        show_video()
        if cv.WaitKey(10) == 27:
            break
