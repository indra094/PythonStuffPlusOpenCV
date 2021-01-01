import cv2
import datetime

#cap2=cv2.VideoCapture('C:\\Users\indra094\Documents\scripts\output.avi')#works for pure video no audio files
cap2=cv2.VideoCapture(0)#device id, 1,2etc in case of multiple cams

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#20.0 ius the fps
out = cv2.VideoWriter('output2.avi', fourcc, 20.0, (640,480))

isOpened = cap2.isOpened()


print(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

#cap2.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
#cap2.set(cv2.CAP_PROP_FRAME_WIDTH, 120)

while isOpened:
    ret, frame = cap2.read()
    #if frame avl ret true otherwise false

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'Width:' + str(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT)) +'HEIGHT:' + str(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame = cv2.putText(frame, text,(10,20), font, 1, (200,40,40), 2)
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, datet, (100,400), font, 1, (100,100,0), 2)
        
    if ret:
        out.write(frame)
    cv2.imshow('Win', frame)
    #cv2.imshow('WinGray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap2.release()
cv2.destroyAllWindows()
    
    
