import cv2 as cv
import numpy as np

# Global variables for HSV values (will be controlled by trackbars)
# Initialize with some default values that work for many cases
low_H = 27
low_S = 108
low_V = 82
high_H = 76
high_S = 255
high_V = 152

# Callback function for trackbars (does nothing, as we read values directly)
def on_trackbar(val):
    pass

# Function to create and initialize trackbars
def create_hsv_trackbars(window_name):
    global low_H, low_S, low_V, high_H, high_S, high_V
    
    cv.createTrackbar("Low H", window_name, low_H, 179, on_trackbar)
    cv.createTrackbar("Low S", window_name, low_S, 255, on_trackbar)
    cv.createTrackbar("Low V", window_name, low_V, 255, on_trackbar)
    cv.createTrackbar("High H", window_name, high_H, 179, on_trackbar)
    cv.createTrackbar("High S", window_name, high_S, 255, on_trackbar)
    cv.createTrackbar("High V", window_name, high_V, 255, on_trackbar)

################
def hsver(frame):
    # Read current values from trackbars
    global low_H, low_S, low_V, high_H, high_S, high_V
    
    # Ensure trackbars exist before trying to read them
    # This might be called before main loop if not careful, so better to read in main loop
    # For simplicity, we'll read them directly in transform function
    
    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))
    return frame_threshold
###################
def medfill(frame):
    median = cv.medianBlur(frame, 5)
    return median
#########################################
def rolling_window(a, window, step_size):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1 - step_size + 1, window)
    strides = a.strides + (a.strides[-1] * step_size,)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)
#####################
def transform(frame, trackbar_window_name):
    global low_H, low_S, low_V, high_H, high_S, high_V

    # Update global HSV values from trackbars
    low_H = cv.getTrackbarPos("Low H", trackbar_window_name)
    low_S = cv.getTrackbarPos("Low S", trackbar_window_name)
    low_V = cv.getTrackbarPos("Low V", trackbar_window_name)
    high_H = cv.getTrackbarPos("High H", trackbar_window_name)
    high_S = cv.getTrackbarPos("High S", trackbar_window_name)
    high_V = cv.getTrackbarPos("High V", trackbar_window_name)

    hsv = hsver(frame)
    ##rolling = rolling_window(hsv,3,1)
    ##final = medfill(rolling)
    return hsv
