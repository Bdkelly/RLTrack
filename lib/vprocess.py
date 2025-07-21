import cv2 as cv
import numpy as np
################
def hsver(frame):
    low = {"H":27,"S":108,"V":82}
    high = {"H":76,"S":255,'V':152}
    ##mask = fgbq.apply(frame,learningRate = 0.02)
    frame_HSV = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV,(low["H"],low["S"],low["V"]),(high["H"],high['S'],high["V"]))
    return frame_threshold
###################
def medfill(frame):
    median = cv.medianBlur(frame,5)
    return median
#########################################
def rolling_window(a, window, step_size):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1 - step_size + 1, window)
    strides = a.strides + (a.strides[-1] * step_size,)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
#####################
def transform(frame):
    hsv= hsver(frame)
    ##rolling = rolling_window(hsv,3,1)
    ##final = medfill(rolling)
    return hsv