import cv2 as cv

img = cv.imread('images\Panda.jpg')
cv.imshow('Panda',img)

# #Converting an image to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)


#How to blur                           #Can help to remove the noise in that image
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)


#Edge Cascade
canny=cv.Canny(blur, 125, 175)
cv.imshow('Canny',canny)


#Dilation 
dilate = cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilate',dilate)

#Erode the dilated image
erode=cv.erode(dilate,(3,3),iterations=1)
cv.imshow('Erode',erode)


#Resize
resize = cv.resize(img, (500,500),interpolation=cv.INTER_AREA)    #interpolation-> shrinking the image/enlarging the image INTER_CUBIC(high quality slower) or INTER_LINEAR
cv.imshow('Resized',resize)


#Crop
crop=img[50:200, 200:400]
cv.imshow('Crop',crop )

cv.waitKey(0)