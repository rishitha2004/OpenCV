import cv2 as cv
img=cv.imread('Photos/lavender.jpg')
cv.imshow('Image',img)
cropped=img[50:250,200:500]
cv.imshow('Cropped',cropped)
cv.waitKey(0)