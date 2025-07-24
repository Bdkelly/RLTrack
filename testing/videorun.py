import cv2 as cv
import numpy as np
from lib.videopro import transform, create_hsv_trackbars # Import create_hsv_trackbars
from lib.ballfind import finder


def main(video):
    dst_window = "Output"
    trackbar_window = "HSV Adjustments" # New window for trackbars
    
    cv.namedWindow(dst_window)
    cv.namedWindow(trackbar_window) # Create the trackbar window

    create_hsv_trackbars(trackbar_window) # Call this function to set up trackbars

    while True:
        ret, frame = video.read()
        if frame is None:
            print("No Frame")
            break
        
        # Resize frame for better performance/view if needed (optional)
        frame = cv.resize(frame, (640, 480)) 

        key = cv.waitKey(10)
        if key == ord('p'):  # Pauses video
            cv.waitKey(-1)
        if key == ord('q'):
            break
        
        # Pass the trackbar window name to transform
        processed = transform(frame, trackbar_window) # Video Processing from lib/videoProcessing.py
        withball,ballcoords = finder(processed)
        print(ballcoords)
        cv.imshow(dst_window, withball)
    
    video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    # Ensure this path is correct for your system
    video_path = r"C:\\Users\Ben\Documents\dever\\python\AI572\\training\\videos\\mlsvideo.mp4" 
    video = cv.VideoCapture(video_path)
    
    if not video.isOpened():
        print(f"Error: Could not open video file at {video_path}")
    else:
        main(video)