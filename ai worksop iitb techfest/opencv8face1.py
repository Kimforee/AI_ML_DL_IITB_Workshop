# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:04:04 2023

@author: AMIT
"""

import cv2
import imutils

face_cascade = cv2.CascadeClassifier("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/haarcascades/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("C:/Users/91821/Desktop/Py playground/aiiitb/OpenCV/haarcascades/haarcascade_smile.xml")

# 0 = CamID (Primary Camera)
vid = cv2.VideoCapture(0)

while 1:
    ret, frame = vid.read()
    # Resize the image
    img_r = imutils.resize(frame, width = 1000)
    
    # Convert Image to grayscale
    gray = cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)
    # 1.3 = threshold value for scale factor, 5 = Num of nearest neighbouring features
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        # Draw the rectangle
        cv2.rectangle(img_r, (x,y),(x+w, y+h), (255,255,255), 1)
        # ROI is region of face
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img_r[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 3.3, 9)
        smile = smile_cascade.detectMultiScale(roi_gray, 3.3, 9)
        for (ex,ey,ew,eh) in eyes:
            # Draw the rectangle
            cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,0,0), 2)
        for (ex,ey,ew,eh) in smile:
            # Draw the rectangle
            cv2.rectangle(roi_color, (ex,ey),(ex+ew, ey+eh), (0,0,0), 2)
    
    
    cv2.imshow('Frame', img_r)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q') or k == 27:
        break               

vid.release()
cv2.destroyAllWindows()