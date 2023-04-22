#Created by SUPARNA DAS

# Taking Image Screenshot using Python OPENCV



import numpy as np
import cv2

cap = cv2.VideoCapture(0)

cv2.namedWindow("test")
img_count = 0


while True:
    ret, frame = cap.read()
    if not ret:
        print("failed")
        break
    cv2.imshow("test", frame)
    k = cv2.waitKey(1)

    if k%256 == 27:
        print("escape hit")
        break
    elif k%256 == 32 :
        img_name = "opencv_frame_{}.png".format(img_count)
        cv2.imwrite(img_name,frame)
        print("screenshot took")
        img_count += 1

cap.release()
cv2.destroyAllWindows()
