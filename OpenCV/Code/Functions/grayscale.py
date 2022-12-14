import cv2 as cv
img=cv.imread('Photos/lavender.jpg')
def rescaleframe(img,scale=0.50):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)
imgresized=rescaleframe(img)
gray=cv.cvtColor(imgresized,cv.COLOR_BGR2GRAY)
cv.imshow("Gray color",gray)
cv.waitKey(0)