

import cv2
import random

def noise_black_white(image):
    # Get the dimensions of Image
    row, col = image.shape
    num_of_pixels = random.randint(1500, 20000)
    for i in range(num_of_pixels):
        # pick random y-coordinate
        y_coordinate = random.randint(0, row - 1)
        # pick random x-coordinate
        x_coordinate = random.randint(0, col - 1)
        image[y_coordinate][x_coordinate] = 255
    for i in range(num_of_pixels):
        # pick random y-coordinate
        y_coordinate = random.randint(0, row - 1)
        # pick random x-coordinate
        x_coordinate = random.randint(0, col - 1)
        image[y_coordinate][x_coordinate] = 0
    return image

image = cv2.imread("E:/OpenCV/parrot.jpg", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/Images/avengers.png",cv2.IMREAD_GRAYSCALE)

cv2.imshow('Original Image', img)
cv2.imshow('Noisy Image',noise_black_white(img))

# cv2.imwrite("E:/OpenCV/noisy_image.jpg",noise_black_white(image))

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()
