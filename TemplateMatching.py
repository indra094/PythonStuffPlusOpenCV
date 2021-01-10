import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\edseye.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(imgGrey, template, cv2.TM_CCOEFF_NORMED)
print (res)
threshold = 0.8
loc = np.where(res >=threshold)
print (loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img,  pt, (pt[0] +w, pt[1]+h), (0,0,255), 2)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
