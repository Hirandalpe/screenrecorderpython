from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

while True :
    image = ImageGrab.grab(bbox=(0, 0, width, height))
    np_array = np.array(image)
    color_correct = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
    cv2.imshow('recorder', color_correct)
    cv2.waitKey(10)
