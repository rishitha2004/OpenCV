import cv2 as cv
img=cv.imread('Photos/lavender.jpg')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Image',resized)
#Averaging
average=cv.blur(resized,(7,7))
cv.imshow('Average Blurred',average)
#gaussian blur
gauss=cv.GaussianBlur(resized,(7,7),0)
cv.imshow('Gauss',gauss)
#median blur
median=cv.medianBlur(resized,7)
cv.imshow('Median Blur',median)
#bilateral
bilateral=cv.bilateralFilter(resized,5,15,25)
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)