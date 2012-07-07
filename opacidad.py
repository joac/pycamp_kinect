#!/usr/bin/env python
import freenect
import cv
import frame_convert
import numpy as np
from utils import alpha_blend, process_depth, alpha_from_depth, load_image_as_array

threshold = 100
current_depth = 0
depth = None
background = load_image_as_array('wallpaper.png')

def change_threshold(value):
    global threshold
    threshold = value


def change_depth(value):
    global current_depth
    current_depth = value


def show_depth():
    global threshold
    global current_depth
    global depth

    depth, timestamp = freenect.sync_get_depth()
   # depth = np.logical_and(depth >= current_depth - threshold,
    #                             depth <= current_depth + threshold)
    depth = process_depth(depth)

    depth8 = depth.astype(np.uint8)

    image = cv.CreateImageHeader(
                                (depth8.shape[1], depth8.shape[0]),
                                 cv.IPL_DEPTH_8U,
                                 1
                                 )
    cv.SetData(
                image,
                depth8.tostring(),
                depth8.dtype.itemsize * depth8.shape[1]
                )

    cv.ShowImage('Depth', image)


def show_video():
    video = freenect.sync_get_video()[0]
    rgba = alpha_from_depth(video, depth) 

    cv.ShowImage('Video', cv.fromarray(video))
    rgb = alpha_blend(rgba, background)
    cv.ShowImage('Video-proceso', cv.fromarray(rgb))



cv.NamedWindow('Depth')
cv.NamedWindow('Video')
cv.CreateTrackbar('threshold', 'Depth', threshold,     500,  change_threshold)
cv.CreateTrackbar('depth',     'Depth', current_depth, 2048, change_depth)
cv.CreateTrackbar('depth',     'Depth', current_depth, 2048, change_depth)

print('Press ESC in window to stop')

if __name__ == '__main__':
    while 1:
        show_depth()
        show_video()
        if cv.WaitKey(10) == 27:
            break
