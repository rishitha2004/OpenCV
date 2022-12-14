import cv2 as cv
import numpy as np
img=cv.imread('Photos/boston.jpg')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)
#To split color channels
b,g,r=cv.split(resized)
# cv.imshow('BLUE',b)
# cv.imshow('GREEN',g)
# cv.imshow('RED',r)
# print(resized.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)
#to merge color channels
# merged=cv.merge([b,g,r])
# cv.imshow('merged image',merged)
#to display same color as that of color channel
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('only blue',blue)
cv.imshow('only green',green)
cv.imshow('only red',red)
cv.waitKey(0)