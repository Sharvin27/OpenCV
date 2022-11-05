import cv2 as cv
import numpy as np

img = cv.imread('images\colors.jpg')

hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

lower_range = np.array([80,50,50])
upper_range = np.array([130,255,255])


mask = cv.inRange(hsv,lower_range,upper_range)

cv.imshow('Orignal',img)
cv.imshow('Color',mask)

cv.waitKey(0)
cv.destroyAllWindows()