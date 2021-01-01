import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

print(cv2.__version__)
img = cv2.imread(r'C:\Users\indra094\Desktop\PENDRIVE\99274.jpg', -1)
img2 = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\chicky_512.png')
#1 rgb, 0 bw, -1 rgba
img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

dst = cv2.add(img, img2)#sums up channels 230 + 240 = 470, cap to 255 so white color
dst2 = cv2.addWeighted(img, .2, img2, .2, 00) #seems to utilize transparency
#img = np.zeros([512,512,4], np.uint8)

print (img.shape)
print (img.dtype)
print (img.size)#no. of pixels

b, g, r = cv2.split(img)#tuples
img = cv2.merge((b, g, r))

img2 = np.zeros((512,512,3), np.uint8)
img2 = cv2.rectangle(img2, (200,0), (300,100), (255,255,255), -1)

#bitAnd = cv2.bitwise_and(img2, dst)
#bitOr = cv2.bitwise_or(img2, dst)
#bitXor = cv2.bitwise_xor(img2, dst)
bitNot1 = cv2.bitwise_not(img2)
bitNot2 = cv2.bitwise_not(dst)

#region of interest- roi
ball = img[140:340, 200:300]#y:y+h, x:x+w
img[0:200, 0:100] = ball
cv2.imshow('win1',img2)
cv2.imshow('win2',dst)
cv2.imshow('bitNot',bitNot2)
cv2.waitKey(0)
cv2.destroyWindow('win1')
#print(img)
img2 = img
#img2.sort()
#print(img2)


def nothing(x):
    print (x)

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('B', 'image', 0, 255, nothing)#trackbar stuff
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0:off\n 1:on'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)
s = 0

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    print (str(r))#int to string
    s = cv2.getTrackbarPos(switch, 'image')

    if s==0:
        pass
    else:
        print ('in 1')
        img[:] = [b,g,r]
        
cv2.destroyWindow('image')

img = cv2.line(img2, (0,200), (255,255), (55,00,57,50), 5) #if 0 in imread no color on line
img = cv2.arrowedLine(img, (0,0), (255,255), (55,200,57,50), 5) #if 0 in imread no color on line

img = cv2.rectangle(img, (230,0), (512,129), (44,66,12,39), 1)#-1 thick to fill
cv2.circle(img, (200,200), 50, 0x77777777, 4)

font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
cv2.putText(img, 'sexy beast', (100,100), font, 1, (100,100,100,100), 1, cv2.LINE_AA)

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print (x,',',y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY = 'superman'
        frm = cv2.putText(img, strXY, (x,y), font, 1, (200,200,40), 1)
        points.append((x,y))
        
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font=cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(blue)+str(green)+str(red)
        #cv2.putText(img, strXY, (x,y), font, 1, (255,255,200), 1)        
        if len(points)>=2:
            cv2.line(img, points[-1], points[-2], (0,200,200), 5)
        myColorImage = np.zeros((512,512,3), np.uint8)
        myColorImage[:] = [blue, green, red]
        cv2.imshow('win2', myColorImage)
        cv2.imshow('window1', img)

cv2.imshow('window1', img)
points = []
cv2.setMouseCallback('window1', click_event)

key = cv2.waitKey(000) & 0xFF
if key==27:#esc
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite('me2.jpg',img2)

cv2.destroyAllWindows()

