
        
roi = img[67:390,447:815]

cv2.imshow("Original", img)
cv2.setMouseCallback('Original', mousePosition)
cv2.imshow("ROI", roi)

# press any key with 0 wait time
cv2.waitKey(0)
# Close all imageframe
cv2.destroyAllWindows()