import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread('Photos/lavender.jpg')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
#cv.imshow('Resized',resized)
# plt.imshow(resized)
# plt.show()
#BGR to gray
# gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)
#BGR to HSV
# hsv=cv.cvtColor(resized,cv.COLOR_BGR2HSV)
# cv.imshow('hsv',hsv)
#BGR to LAB
# lab=cv.cvtColor(resized,cv.COLOR_BGR2LAB)
# cv.imshow('lab',lab)
#BGR to RGB
# rgb=cv.cvtColor(resized,cv.COLOR_BGR2RGB)
# cv.imshow('rgb',rgb)
#HSV to BGR
# hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
# cv.imshow('bgr',hsv_bgr)
cv.waitKey(0)