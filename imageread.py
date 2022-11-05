import cv2 as cv

# Reads the image

img=cv.imread("images\cat.webp")                  

cv.imshow('Cat',img)


#Resizing the image
def rescaleFrame(frame, scale=0.75):           #Works for Image videos and live vids
    width = int(frame.shape[1] * scale)        #frame.shape[1] is width of your image and frame.shape[0] is height
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# cv.waitKey(0)

img_resized=rescaleFrame(img,scale=.2)      #IMAGE RESIZING

cv.imshow('Cat Resize',img_resized)


def changeRes(width,height):                   #capture.set fn works for live videos
    capture.set(3,width)                       #3 references the width and 4 references the height
    capture.set(4,height)

#Reading a video


capture=cv.VideoCapture(0)

while True:
    isTrue, frame=capture.read()                   #Bolean value , frame

    frame_resized=rescaleFrame(frame, scale=.2)

    cv.imshow('Video',frame)

    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):            #press d and it will get released
        break

capture.release()
cv.destroyAllWindows()



