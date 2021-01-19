import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture(r'C:\opencv-master\opencv-master\samples\data\vtest.avi')

fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows = False)

while True:
    _, img = cap.read()

    fgmask = fgbg.apply(img)
    cv2.imshow('fgmask', fgmask)
    
    cv2.imshow('Video', img)
    if cv2.waitKey(1) % 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
