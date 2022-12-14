import cv2 as cv
img=cv.imread('Photos/boston.jpg')
cv.imshow('image',img)
def rescaleframe(img,scale=0.75):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)
img_resized=rescaleframe(img,0.25)
cv.imshow('ResizedImage',img_resized)
cv.waitKey(0)