import cv2 as cv
import numpy as np
#to create a blank place
blank=np.zeros((500,500,3),dtype='uint8')
#to draw border of thickness 2px
#cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=2)
#to fill rectangle with color
#cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=cv.FILLED)
#(OR)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,0,255),thickness=-1)
#(OR)
#cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=-1)
cv.imshow('Rectangle',blank)
cv.waitKey(0)