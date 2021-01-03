import numpy as np
import cv2

img1 = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\boy.png')
img2 = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\girl2.jpg')

print (img1.shape)
print (img2.shape)

orapple = np.hstack((img1[:, :93], img2[:, 93:]))

applecopy = img1.copy()
gpapple = [applecopy]#gaussianpyr

for i in range(6):
    applecopy = cv2.pyrDown(applecopy)
    gpapple.append(applecopy)

orangecopy = img2.copy()
gporange = [orangecopy]

for i in range(6):
    orangecopy = cv2.pyrDown(orangecopy)
    gporange.append(orangecopy)
    

applecopy = gpapple[5]
lpapple = [applecopy]#laplacianpyr

for i in range(5,0,-1):
    gaussianexpanded = cv2.pyrUp(gpapple[i])
    laplacian = cv2.subtract(gpapple[i-1], gaussianexpanded)#cols and rows should be the same
    #cv2.imshow(str(i), laplacian)
    lpapple.append(laplacian)

orgcopy = gporange[5]
lporg = [orgcopy]


for i in range(5,0,-1):
    gaussianexpanded = cv2.pyrUp(gporange[i])
    laplacian = cv2.subtract(gporange[i-1], gaussianexpanded)
    print ("lap shape", laplacian.shape)
    lporg.append(laplacian)

appleorgpyr = []
n = 0
for applelap, orglap in zip(lpapple, lporg):
    n+=1
    cols, rows, ch = applelap.shape
    print (cols, rows, ch)
    laplacian = np.hstack((applelap[:, 0:int(cols* 93.0/256.0)], orglap[:, int(cols* 93.0/256):]))
    appleorgpyr.append(laplacian)

#laplacian images are till index 1 but gaussian images are till index 0
#image is reconstructed by expanding 0image and then adding laplacian difference
# at index 1- basically the edges will end up becoming blurred
appleorgrecon = appleorgpyr[0]

for i in range(1,6):
    appleorgrecon = cv2.pyrUp(appleorgrecon)
    #cv2.imshow("appleorgrecon"+str(i), appleorgrecon)
    #cv2.imshow("appleorgpyri", appleorgpyr[i])
cv2.imshow("appleorgreconblurrr", appleorgrecon)

orgrecon = lporg[0]

for i in range(1,6):
    orgrecon = cv2.pyrUp(orgrecon)
    #cv2.imshow("appleorgrecon"+str(i), appleorgrecon)
    #cv2.imshow("appleorgpyri", appleorgpyr[i])
    orgrecon = cv2.add(lporg[i], orgrecon)
cv2.imshow("orgrecon", orgrecon)


appleorgrecon = appleorgpyr[0]    
#cv2.imshow("appleorgpyr[0]"+str(0), appleorgpyr[0])
#cv2.imshow("appleorgpyr1", appleorgpyr[1])
for i in range(1,6):
    appleorgrecon = cv2.pyrUp(appleorgrecon)
    #cv2.imshow("appleorgrecon"+str(i), appleorgrecon)
    #cv2.imshow("appleorgpyri", appleorgpyr[i])
    appleorgrecon = cv2.add(appleorgpyr[i], appleorgrecon)

    
cv2.imshow("Apple", img1)
cv2.imshow("Orange", img2)
cv2.imshow("appleorange", orapple)
cv2.imshow("Appleorangerecon", appleorgrecon)

cv2.waitKey(0)
cv2.destroyAllWindows()
