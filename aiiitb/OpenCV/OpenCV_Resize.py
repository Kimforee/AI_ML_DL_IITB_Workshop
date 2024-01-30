
import cv2
import imutils

img = cv2.imread("aiiitb\OpenCV\Images\pug.jpg")

# It takes height and width of image and reshapes to 500x500
img_resize = cv2.resize(img, (700,700))

img_resize1 = imutils.resize(img, width = 900)

cv2.imshow('Original', img)
cv2.imshow('Reshape', img_resize)
cv2.imshow('Reshape1', img_resize1)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()
