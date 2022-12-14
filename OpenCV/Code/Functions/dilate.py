import cv2 as cv
img=cv.imread('Photos/boston.jpg')
canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)
dilated=cv.dilate(canny,(5,5),iterations=1)
#can even use image in place of canny
#iterations increases the thickness of dilated edges
#kernel size increases the dilation increases
cv.imshow('Dilated',dilated)
cv.waitKey(0)