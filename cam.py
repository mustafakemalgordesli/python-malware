# cam.py
import numpy as np
import cv2 as cv
import logging
import uuid
import time

def cap_init():
    return cv.VideoCapture(0)     


logging.basicConfig(filename=("error.txt"), level=logging.ERROR, format=" %(asctime)s - %(message)s")


def cam_record():
    print("Cam record starting")
    while True:
        cap = cap_init()
        if not cap.isOpened():
            logging.error("Cannot open camera")
        else: 
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                logging.error("Can't receive frame (stream end?). Exiting ...")
            else:
                # cv.imwrite("captures/opencv"+str(uuid.uuid1())+".jpg", frame)
                cv.imwrite("captures/opencv.jpg", frame)
                cap.release()
                cv.destroyAllWindows()
                del(cap)
        time.sleep(10)

# cam_record()
    

