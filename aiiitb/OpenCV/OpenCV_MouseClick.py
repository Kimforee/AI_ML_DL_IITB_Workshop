import cv2
import numpy as np

circles = np.zeros((4,2), int)
counter = 0

def mousePosition(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter += 1
        print(circles)
        
img = cv2.imread("aiiitb/OpenCV/Images/avengers.png")

cv2.imshow("Original", img)
cv2.setMouseCallback('Original', mousePosition)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()