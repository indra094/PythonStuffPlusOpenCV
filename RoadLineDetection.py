import numpy as np
import cv2

def roif(img, verts):
    mask = np.zeros_like(img)
    #channel_count = img.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask, verts, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def drawlines(img, lines):
    img2 = np.copy(img)
    blnkimg = np.zeros((img2.shape[0],img2.shape[1],3), dtype=np.uint8)

    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blnkimg, (x1,y1), (x2,y2), (0,255,0), thickness = 3)

    img2 = cv2.addWeighted(img2, 0.8, blnkimg, 1, 0.0)
    return img2

def process(img):
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_img = cv2.Canny(gray_img, 100, 200)
    cv2.imshow("canny_img", canny_img)

    roi = [
        (0, img.shape[0]),
        (img.shape[1]/2 - 80, img.shape[0]/2),
        (img.shape[1]/2 - 60, img.shape[0]/2),
        (img.shape[1], img.shape[0] - 50),
        (img.shape[1], img.shape[0])
    ]

    cropped_img = roif(canny_img, np.array([roi], np.int32))
    cv2.imshow("cropped_img", cropped_img)

    lines = cv2.HoughLinesP(cropped_img, rho = 2, theta = np.pi*1/180,threshold=50,
                        lines=np.array([]),minLineLength = 40,maxLineGap=25)

    if lines is not None:
        imgwithlines = drawlines(img, lines)
        return imgwithlines
    else:
        return img

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
