import numpy as np
import cv2 as cv
from config import config
from asyncio import sleep
from models.camera import Camera


async def video_capture(camera: Camera):
    cap = cv.VideoCapture(camera.url)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        retval, current_frame = cv.imencode('.jpg', frame)
        camera.current_frame = current_frame.tobytes()
        await sleep(0)
    # Release everything if job is finished
    cap.release()
    cv.destroyAllWindows()