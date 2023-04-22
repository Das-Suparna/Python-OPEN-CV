#Code for opening video cam using PYTHON OPENCV
#created by Suparna Das

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q') :
        break
cap.release()
cv2.destroyAllWindows()
