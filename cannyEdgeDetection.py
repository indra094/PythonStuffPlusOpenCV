import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png',0)
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

canny = cv2.Canny(img, 0, 255)

cv2.imshow("canny", canny)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
