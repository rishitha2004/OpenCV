import cv2 as cv
img=cv.imread('Photos/boston.jpg')
canny=cv.Canny(img,125,175)
dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)
cv.waitKey(0)