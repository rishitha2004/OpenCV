import cv2 as cv
import numpy as np
img=cv.imread('Photos/boston.jpg')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
blank=np.zeros((500,500),dtype='uint8')
masks=cv.circle(blank,(250,250),100,255,-1)
masked=cv.bitwise_and(resized,resized,mask=masks)
cv.imshow('masked',masked)
cv.waitKey(0)