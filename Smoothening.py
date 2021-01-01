import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
#low pass filter- for blurring, high pf for edge detection
blur = cv2.blur(img, (5,5))
#gaussian filters have higher weight towards the center
gauss = cv2.GaussianBlur(img, (5,5), 0)

#salt and pepper noise - white and black noise use median blur
med = cv2.medianBlur(img, 5)

#for preserving borders, use bilateral filters
bil = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Image", img)
#cv2.imshow("dst", dst)
cv2.imshow("blur", blur)
cv2.imshow("gaussss", gauss)
cv2.imshow("med", med)
cv2.imshow("bilateral", bil)

cv2.waitKey(0)
cv2.destroyAllWindows()
