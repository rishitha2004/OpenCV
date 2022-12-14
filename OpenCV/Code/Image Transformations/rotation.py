import cv2 as cv
img=cv.imread('Photos/dog.jpg')
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)
def rotation(resized,angle,rotPoint=None):
    (height,width)=resized.shape[:2]
    if(rotPoint==None):
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    cv.warpAffine(resized,rotMat,dimensions)
rotated=rotation(resized,45,None)
cv.imshow('Rotated',rotated)
cv.waitKey(0)