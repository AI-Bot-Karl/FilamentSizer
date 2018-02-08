import cv2
import numpy

a=numpy.pi

print(a)

cap = cv2.VideoCapture(0)

while (True):

    #capture video freame by frame
    ret, frame = cap.read()

    #display results
    cv2.imshow('Frame', frame)

    #wait for pressing q to end program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 #final routines to close video stream properly
cap.release()
cv2.destroyAllWindows
