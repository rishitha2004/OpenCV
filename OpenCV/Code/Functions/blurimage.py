import cv2 as cv
img=cv.imread('Photos/boston.jpg')
cv.imshow('Image',img)
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)