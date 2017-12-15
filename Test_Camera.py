import cv2
import numpy as np

#Assign the video capture
cap = cv2.VideoCapture(0)

while (True):
    #capture video freame by frame
    ret, frame = cap.read()

    #get gray colored version
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #get R,G,B version
    r,g,b = cv2.split(frame)

    #display results
    cv2.imshow('Gray', gray)
    cv2.imshow('Frame', frame)
    cv2.imshow('red', r)
    cv2.imshow('green', g)
    cv2.imshow('blue', b)

    #wait for pressing q to end program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#final routines to close video stream properly
cap.release()
cv2.destroyAllWindows
