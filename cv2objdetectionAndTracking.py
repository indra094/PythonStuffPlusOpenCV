import cv2
import numpy as np

def nothing(x):
    a=1+2

cap = cv2.VideoCapture(0)

cv2.namedWindow("T")
cv2.createTrackbar("LH", "T", 0, 255, nothing)
cv2.createTrackbar("LS", "T", 0, 255, nothing)
cv2.createTrackbar("LV", "T", 0, 255, nothing)
cv2.createTrackbar("UH", "T", 255, 255, nothing)
cv2.createTrackbar("US", "T", 255, 255, nothing)
cv2.createTrackbar("UV", "T", 255, 255, nothing)

while 1:
    #frame = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')
    #frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "T")#hue base pigment
    l_s = cv2.getTrackbarPos("LS", "T")#saturation is amount of color
    l_v = cv2.getTrackbarPos("LV", "T")#value is brightness

    u_h = cv2.getTrackbarPos("UH", "T")
    u_s = cv2.getTrackbarPos("US", "T")
    u_v = cv2.getTrackbarPos("UV", "T")

    #print (str(l_h) + str(l_s))

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])#For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255].

    mask = cv2.inRange(hsv, l_b, u_b)#set to 255 1 channel
    #print (mask.shape)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    def click_event(event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONDOWN:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hue = hsv[y, x, 0]
            sat = hsv[y, x, 1]
            val = hsv[y, x, 2]
            strXY = 'H='+str(hue)+'S='+str(sat)+'V='+str(val)
        #cv2.putText(img, strXY, (x,y), font, 1, (255,255,200), 1)        
            print (strXY)
        
    cv2.imshow('frame', frame)
    cv2.setMouseCallback('frame', click_event)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1) & 0xff
    if key==27:
        break

cap.release()
cv2.destroyAllWindows()
    
