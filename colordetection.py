import cv2 as cv

# img = cv.imread('images\\blue.jpg')

# print(img)
# cv.imshow('Blue',img)


cap = cv.VideoCapture(0)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 880)            #set size
cap.set(cv.CAP_PROP_FRAME_HEIGHT,520)

while True:
    _, frame=cap.read()
    hsv_frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    height,width,_ = frame.shape

    cx =width//2
    cy =height//2

    #Pick Pixel Value
    pixel_center = hsv_frame[cy, cx]

    hue_value = pixel_center[0]

    color="Undefined"
    if hue_value<5:
        color="Red"
    elif hue_value < 22:
        color = "Orange"
    elif hue_value <33:
        color="Yellow"
    elif hue_value <78:
        color="Green"
    elif hue_value <131:
        color="Blue"
    elif hue_value < 178:
        color="Violet"
    else:
        color = "Red"
    

    print(pixel_center)

    pixel_center_bgr= frame[cy,cx]
    b, g, r=int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv.putText(frame, color,(20,50), 0, 1.5,(b,g,r),2)
    cv.circle(frame, (cx,cy), 5 ,(2525,25),2)


    cv.imshow('Video',frame)

    if cv.waitKey(2) & 0xFF==ord('d'):            #press d and it will get released
        break

cap.release()
cv.destroyAllWindows()


cv.waitKey(0)

