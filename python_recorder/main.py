from PIL import ImageGrab
import numpy as np
import cv2

while True :
    image = ImageGrab.grab(bbox=(0, 0, 1360, 780))
    np_array = np.array(image)
    color_correct = cv2.cvtColor(np_array, cv2.COLOR_BGR2RGB)
    cv2.imshow('recorder', color_correct)
    cv2.waitKey(10)