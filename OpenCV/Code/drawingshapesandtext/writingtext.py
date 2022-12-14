import cv2 as cv
import numpy as np
blank=np.zeros((500,500,3),dtype='uint8')
cv.putText(blank,'Hello!!I am Rishitha',(20,300),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),thickness=2)
cv.imshow('Write',blank)
cv.waitKey(0)