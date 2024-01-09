import cv2

img = cv2.imread("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/Images/avengers.png")
cv2.imshow('Original', img)

print(img)

# convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()