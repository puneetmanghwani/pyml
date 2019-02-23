#!/usr/bin/python3

import cv2,time

cap=cv2.VideoCapture('http://10.255.73.221:8080/video?x.mjpg')
face_cascade = cv2.CascadeClassifier('/home/punit/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/punit/haarcascades/haarcascade_eye.xml')
def detect_face_eyes(img):
    
  
    face_img = img.copy()
  
    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2) 
    eyes = eye_cascade.detectMultiScale(face_img) 
    for (x,y,w,h) in face_rects: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10) 
    for (x,y,w,h) in eyes: 
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10)     
    return face_img



while cap.isOpened():
    status,frame=cap.read()
    frame=detect_face_eyes(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('camera',frame)
    if cv2.waitKey(1) & 0xFF == ord('q') :
       break
        
cap.release()
cv2.destroyAllWindows()
