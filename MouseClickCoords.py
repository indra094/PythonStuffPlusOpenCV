import cv2

posList = []
def onMouse(event, x, y, flags, param):
   global posList
   if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = cv2.imread(r"C:/Users/indra094/Documents/scripts/95_right.jpeg", 1)
windowName = "Window1"
cv2.imshow(windowName, img)

cv2.setMouseCallback(windowName, onMouse)
#print(posList[0])
