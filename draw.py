import cv2 as cv
import numpy as np


#Creating a blank image
blank = np.zeros((500,500,3), dtype='uint8')         #uint8 is datatype of an image   / (height width and no. of colour channels)
cv.imshow('Blank',blank)

#Painting the image a certain color
# blank[:]=0,255,0                                      #[:] means for all pixels

# blank[200:300, 300:400]=0,0,255
# cv.imshow('Green',blank)


# Draw a rectangle
# cv.rectangle(blank, (0,0), (200,500), (0,0,255) ,thickness=2)

# cv.rectangle(blank,(0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=cv.FILLED)   #Fills the rectangle with FILLED or -1
# cv.imshow('Rectangle',blank)


#Draw a circle
# cv.circle(blank,(250,250),40,(0,255,255),thickness=4)
# cv.imshow('Circle',blank)


# #Draw a line
# cv.line(blank,(0,0), (200,500), (0,0,255) ,thickness=3)
# cv.imshow('Line',blank)


#Write text on an image
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0,(0,225,255), 2) 
cv.imshow('Text',blank)

cv.waitKey(0)