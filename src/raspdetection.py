from picamera.array import PiRGBArray
from picamera import picamera
import numpy as np
import cv2
import time

# Loads haar cascades for facial detection reference.\
face_cascade = cv2.CascadeClassifier(
    '/Users/ariveralee/opencv/data/lbpcascades/lbpcascade_frontalface.xml')


camera = PiCamera()						# initialize camera
camera.resolution = (320, 240)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(320, 240))


count = 0 								# counter for face detection


time.sleep(0.1)							# allow camera to initialize

# Takes in each frame from the camera and converts it to OpenCv's BGR format
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True)
	img = frame.array
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.5, 3)
	
	if len(faces) != 0:					# not zero if a face is detected
		count += 1
	
	# Draws the rectangle around the face
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)



	cv2.imshow("Camera Feed", img)		# Uses a GUI to display each frame
	key = cv2.waitKey(1) & 0xFF			# Wait key to keep the video streaming
	rawCapture.truncate(0)				# removes each frame after it's displayed

	if count == 30:						# if the face was visible in 30 frames
		count = 0 						# reset the count
		print("Found a human")
	
	if key == ord("q"):					# Pressing q quits the program			
		break

print(count) 							# for Testing
cv2.destroyAllWindows() 
