import imutils
import cv2
face_cascade = cv2.CascadeClassifier("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/haarcascades/haarcascade_eye.xml")

img = cv2.imread("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/Images/avengers.png")
vid = cv2.VideoCapture(0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(  gray,
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
while 1:
    for (x,y,w,h) in faces:
            # Draw the rectangle
            cv2.rectangle(img, (x,y),(x+w, y+h), (255,255,255), 1)
            # ROI is region of face
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 1)
            for (ex,ey,ew,eh) in eyes:
                # Draw the rectangle
                cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,0,0), 2)
        
    cv2.imshow('Frame', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break  

vid.release()
cv2.destroyAllWindows()