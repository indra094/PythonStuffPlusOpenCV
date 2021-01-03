import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png',0)
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

#gradient stuff
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)#To handle negative slope or float not sure how
lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)#1 for dx to use sobelx method
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelComb = cv2.bitwise_or(sobelX, sobelY)

cv2.imshow("sobelComb", sobelComb)
cv2.imshow("SOBELX", sobelX)
cv2.imshow("SOBELY", sobelY)

cv2.waitKey(0)
cv2.destroyAllWindows()
