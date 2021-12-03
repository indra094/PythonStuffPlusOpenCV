import numpy as np
import cv2

img = cv2.imread(r'C:\Users\indra094\Documents\scripts\ResultImages\veins1.jpeg')
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imggray, 127, 255, 0)
kernel = np.ones((2,2), np.uint8)

#dilation = cv2.dilate(thresh, kernel, iterations=1)
erosion = cv2.erode(thresh, kernel, iterations=5)
dilation = cv2.dilate(erosion, kernel, iterations=5)

  
# Find Canny edges
edges = cv2.Canny(dilation, 30, 200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

i=0
for cnt in contours:
    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)
    #cv2.imshow("orig2"+str(i), approx)
    print (cv2.arcLength(cnt,True))
    print (cv2.contourArea(cnt))
    i +=1
#COUNTOURS vector of x,y - boundary points

print (len(contours))
#print (contours[1])

cv2.drawContours(dilation, contours, -1, (0, 255, 0), 1)

cv2.imshow("orig", dilation)
cv2.imshow("eroded", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
