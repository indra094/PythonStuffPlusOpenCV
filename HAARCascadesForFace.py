import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(r'C:\opencv-master\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade =  cv2.CascadeClassifier(r'C:\opencv-master\opencv-master\data\haarcascades\haarcascade_eye.xml')

#img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\boy.png')
#frame = cv2.imread(r'C:\opencv-master\opencv-master\samples\data\smarties.png')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()
    #img = cv2.imread(r'C:\Users\indra094\Pictures\Camera Roll\EDS.png')

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,255), 2)
        
    cv2.imshow('img', img)
    if cv2.waitKey(1) % 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
