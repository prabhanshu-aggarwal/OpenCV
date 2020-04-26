# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:32:47 2020

@author: Prabhanshu Aggarwal
"""
import cv2
cap = cv2.VideoCapture(0)   
print(cap.isOpened()) 
cap.set(3,700)
cap.set(4,700)

while(True):
    ret, frame = cap.read()
    print(cap.get(3))
    print(cap.get(4))
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()