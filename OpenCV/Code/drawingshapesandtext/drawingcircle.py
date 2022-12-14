import cv2 as cv
import numpy as np
#to create a blank place
blank=np.zeros((500,500,3),dtype='uint8')
cv.circle(blank,(250,250),40,(255,0,0),thickness=-1)
cv.imshow('Circle',blank)
cv.waitKey(0)