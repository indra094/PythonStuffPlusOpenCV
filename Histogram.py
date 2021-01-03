import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
