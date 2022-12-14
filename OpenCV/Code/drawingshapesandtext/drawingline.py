import cv2 as cv
import numpy as np
#to create a blank place
blank=np.zeros((500,500,3),dtype='uint8')
cv.line(blank,(0,0),(250,250),(0,255,0),thickness=3)
cv.imshow('Line',blank)
cv.waitKey(0)