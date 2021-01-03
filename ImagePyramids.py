import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

img2 = img.copy()
gp = (img2)

for i in range(6):
    img2 = cv2.pyrDown(img2)
    np.append(gp, img2)
    #cv2.imshow(str(i), img2)

img2 = gp[5]
#cv2.imshow('upper level Gaussian Pyramid', img2)
lp = [img2] #layer in laplacian pyr = upper layer in gaussian pyr - expanded version layer in gaussian pyr

for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp[i])
    print(gaussian_extended.shape, gp[i-1].shape)
    laplacian = cv2.subtract(gp[i-1], gp[i])
    cv2.imshow(str(i), laplacian)
    #for blending and reconstruction of images

lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

ur1 = cv2.pyrUp(cv2.pyrUp(lr2))

#cv2.imshow("Image", img)
#cv2.imshow("ur1", ur1)

cv2.waitKey(0)
cv2.destroyAllWindows()
