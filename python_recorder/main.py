import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
filename = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video_cap = cv2.VideoWriter(filename, fourcc, 20.0, (width, height))


while True :
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    np_array = np.array(image)
    color_correct = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
    cv2.imshow('recorder', color_correct)
    video_cap.write(np_array)
    if cv2.waitKey(10) == ord('s'):
        break

