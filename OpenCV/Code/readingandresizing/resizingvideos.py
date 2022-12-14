import cv2 as cv
capture=cv.VideoCapture('Videos/Doggy.mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    def rescaleframe(frame,scale=0.75):
        width=int(frame.shape[1]*scale)
        height=int(frame.shape[0]*scale)
        dimensions=(width,height)
        return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    frame_resized=rescaleframe(frame,0.25)
    cv.imshow('Resized',frame_resized)
    if cv.waitKey(20)&0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()