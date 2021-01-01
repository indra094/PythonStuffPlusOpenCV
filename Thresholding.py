import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png', 0)
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)#_ is the threshold value
_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)#_ is the threshold value
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)#_ is the threshold value
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#_ is the threshold value
_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)#_ is the threshold value

cv2.imshow("img", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.imshow("th4", th4)
cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
