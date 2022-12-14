import cv2 as cv
img=cv.imread('Photos/dog.jpg')
cv.imshow('Image',img)
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)
cv.waitKey(0)