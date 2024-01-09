import cv2

# 0 is for cam1, 1 for 2 and so on
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 

# run main loop
# if we show one image after antoher, it becomes video
while True:
    ret, frame = cap.read()          # read from camera
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	# output the frame 
    out.write(hsv) 
	# The original input frame is shown in the window 
    cv2.imshow('Original', frame)
    cv2.imshow('frame',hsv)         # show image
    if cv2.waitKey(10) == ord('q'):  # wait a bit, and see keyboard press
        break                        # if q pressed, quit

# release things before quiting
cap.release()
cv2.destroyAllWindows()