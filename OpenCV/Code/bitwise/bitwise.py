import cv2 as cv
import numpy as np
blank=np.zeros((500,500),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
cv.imshow('Rectangle',rectangle)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Circle',circle)
#Bitwise and
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('and',bitwise_and)
#Bitwise OR
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('or',bitwise_or)
#Bitwise XOR
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('xor',bitwise_xor)
#Bitwise NOT
bitwise_not_rec=cv.bitwise_not(rectangle)
cv.imshow('not-rec',bitwise_not_rec)
bitwise_not_cir=cv.bitwise_not(circle)
cv.imshow('circle',bitwise_not_cir)
cv.waitKey(0)