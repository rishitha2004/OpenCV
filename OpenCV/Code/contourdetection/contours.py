import cv2 as cv
import numpy as np
img=cv.imread('Photos/boston.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blank=np.zeros(img.shape[:2],dtype='uint8')
#cv.imshow('gray',gray)
# canny=cv.Canny(img,125,175)
# cv.imshow('Canny Edges',canny)
# contours,hierarchies=cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
#Passing threshold
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
contours,hierarchies=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(len(contours))
cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours drawn',blank)
cv.waitKey(0)
