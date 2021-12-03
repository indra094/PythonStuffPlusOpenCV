import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Documents\scripts\ResultImages\veins3.jpeg', 0)
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)#_ is the threshold value
#_, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)#_ is the threshold value
#_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)#_ is the threshold value
#_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)#_ is the threshold value
#_, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)#_ is the threshold value

th2 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 5)
th3 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 5)

kernel = np.ones((2,2), np.uint8)

#erosion = cv2.erode(th3, kernel, iterations=1)
#dilation = cv2.dilate(erosion, kernel, iterations=1)
#morphology stuff
opn = cv2.morphologyEx(th2, cv2.MORPH_OPEN, kernel) #erosion followed by dilation - white foregrdound black bg
cls = cv2.morphologyEx(th2, cv2.MORPH_CLOSE, kernel) # dilation followed by erosion

cv2.imshow("img", img)
cv2.imshow("th3", th2)
cv2.imshow("opn", opn)
cv2.imshow("cls", cls)
#cv2.imshow("th4", th4)
#cv2.imshow("th5", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
