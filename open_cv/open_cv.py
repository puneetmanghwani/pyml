#!/usr/bin/python3

import cv2,time

cap=cv2.VideoCapture(0)
i=0
while cap.isOpened():
    #  here status return true or false 
    # frame is the actual data captured by camera
    status,frame=cap.read()
    height,width=frame.shape[:2]

    crop_frame=frame[0:int(height/2),0:int(width/2)]
    # converting image from color to gray 
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('camera0',frame)
    cv2.imshow('camera1',frame)
    cv2.imshow('camera2',crop_frame)
    #cv2.imshow('camera3',gray)
    cv2.imwrite('pic{}.jpg'.format(i), frame)
    i+=1 
    if cv2.waitKey(1) & 0xFF == ord('q') :
        
        break

cap.release()
cv2.destroyAllWindows()
