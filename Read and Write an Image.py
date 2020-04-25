# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 00:34:44 2020

@author: Prabhanshu Aggarwal
"""
import cv2

img = cv2.imread('lena.jpg')

print(img)

cv2.imshow('image',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()

cv2.imwrite('lena_new.png', img)

cv2.imshow('image',img)
k = cv2.waitKey(1) & 0xFF == ord('q')

if k==27:
    cv2.imwrite('lena_new1.png', img)
    cv2.destroyAllWindows()
elif k == ord('c'):
    cv2.imwrite('lena_new1.png', img)
    cv2.destroyAllWindows()
