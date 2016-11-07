import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(
    '/Users/ariveralee/opencv/data/lbpcascades/lbpcascade_frontalface.xml')

cap = cv2.VideoCapture(0)
cap.set(3, 320)  # resize the frame
cap.set(4, 240)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 2)  # looks for the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('Camera Feed', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # pressing q exits
        break

cap.release()
cv2.destroyAllWindows()
