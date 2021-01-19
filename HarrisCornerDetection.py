import numpy as np
import cv2

#img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
img = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\chessboard.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

print (dst.shape)

img[dst>0.01*dst.max()] = [0,0,255]


cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
