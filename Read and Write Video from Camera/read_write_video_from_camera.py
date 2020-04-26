# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:37:14 2020

@author: Prabhanshu Aggarwal
"""
import cv2

cap = cv2.VideoCapture(0)   
print(cap.isOpened()) 

fourcc = cv2.VideoWriter_fourcc(*'XVID')   
out = cv2.VideoWriter('output.avi' , fourcc, 20, (640,480))    

while(True):
    ret, frame = cap.read()
    if(ret == True):
  
        out.write(frame)
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        print(cap.get(3))
        print(cap.get(4))
       
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()