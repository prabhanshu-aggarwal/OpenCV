# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:10:58 2020

@author: Prabhanshu Aggarwal
"""
#import the OpenCV library
import cv2

#Loading the Cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#define the functions that will do the detection
def detect(gray, frame):
    #It returns the tupes of rectangle(upper left top coordinates[x,y], height , weight)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y,w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)
    return frame

#Face Recognition with Web Cam
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    frame=cv2.flip(frame,1,0) 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video', canvas)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()

