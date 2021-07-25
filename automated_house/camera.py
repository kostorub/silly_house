import numpy as np
import cv2 as cv
from config import config
from time import sleep
from traceback import format_exc


def video_capture(camera):
    while True:
        try:
            cap = cv.VideoCapture(camera.url)

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    break
                retval, current_frame = cv.imencode('.jpg', frame)
                camera.current_frame = current_frame.tobytes()
                sleep(0)
            # Release everything if job is finished
            cap.release()
            cv.destroyAllWindows()
        except BrokenPipeError:
            break
        except Exception as e:
            print(e)
            print(format_exc())
        sleep(10)
