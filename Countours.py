import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imggray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#COUNTOURS vector of x,y - boundary points

print (str(len(contours)))

cv2.drawContours(img, contours, -1, (0, 200, 0), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
