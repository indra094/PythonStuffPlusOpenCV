import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(r'C:\opencv-master\opencv-master\samples\data\vtest.avi')
while cap.isOpened():
    _, frm = cap.read()

    if frm is None:
        break

    cv2.imshow('Video', frm)
    if cv2.waitKey(1) % 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
