import cv2

img = cv2.imread("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/Images/avengers.png")

re = cv2.resize(img,(525, 350))
cv2.imshow('original',re)

can = cv2.Canny(re,50,300)
cv2.imshow('edge detection using canny filter',can)

cv2.waitKey(0)
cv2.destroyAllWindows()