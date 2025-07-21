import cv2 as cv
import numpy as np
from lib.vprocess import transform
from lib.balldet import finder


def main(video):
    dst_window ="Output"
    while True:
        ret,frame = video.read()
        if frame is None:
            print("No Frame")
            break
        key = cv.waitKey(10)
        if key == ord('p'):#Pauses video
            cv.waitKey(-1)
        if key == ord('q'):
            break
        processed = transform(frame)#Video Proccessing from lib/videoProcessing.py
        cv.imshow(dst_window,processed)
    video.release()
    cv.destroyAllWindows()




if __name__ == "__main__":
    cap = 'video\\mlsvideo.mp4'
    video = cv.VideoCapture(r"video\\mlsvideo.mp4")
    main(video)