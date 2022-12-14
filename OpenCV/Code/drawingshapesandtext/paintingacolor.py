import cv2 as cv
import numpy as np
#to create a blank place
blank=np.zeros((500,500,3),dtype='uint8')
blank[200:300,300:400]=(0,0,255)
cv.imshow('Green',blank)
cv.waitKey(0)