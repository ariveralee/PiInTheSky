import numpy as np
import cv2

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('/Users/ariveralee/opencv/data/lbpcascades/lbpcascade_frontalface.xml')

#this is running incredibly slow on the mac. Need to make faster.

cap = cv2.VideoCapture(0)

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    resized_image = cv2.resize(img, (500, 400)) # resize the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # looking for the faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h),(255,0,0), 2) # draw the square
        
    cv2.imshow('img', resized_image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
