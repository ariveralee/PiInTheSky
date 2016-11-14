from picamera.array import PiRGBArray
from gpiozero import MotionSensor
import picamera
import numpy as np
import cv2
import time

# Loads haar cascades for facial detection reference
face_cascade = cv2.CascadeClassifier(
    '/home/pi/opencv-3.1.0/data/lbpcascades/lbpcascade_frontalface.xml')

MIN_FACE_COUNT = 15                 # min frames before we detected a person
MIN_FRAMES = 120                    # frames needed w.o a face before we stop searching
FACE_COUNTER = 0                    # increments for each frame a face is found
NO_FACE = MIN_FRAMES                # when zero, shuts off camera.
EXIT_PROGRAM = 0                    # When 1, program quits
WINDOW_NAME = "Security feed"       # Window name for feed
MOTION_SENSOR = MotionSensor(4)     # motion sensor sends output to pin 4

# runs indefinitely until we quit.
while True:
    print("Waiting for motion")
    # pauses program until motion is detected
    MOTION_SENSOR.wait_for_motion()
    print("Motion detected!")

    if MOTION_SENSOR.motion_detected == True:
        # create the camera object
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 30
        rawCapture = PiRGBArray(camera, size=(640, 480))
        # allows camera to initialize
        time.sleep(0.1)

        # Takes in each frame from the camera and converts it to OpenCv's BGR
        # format. When a face is found in each frame, a rectangle is drawn.
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            img = frame.array
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.namedWindow(WINDOW_NAME)
            faces = face_cascade.detectMultiScale(gray, 1.5, 3)

            if len(faces) != 0:		# not zero if a face is detected
                FACE_COUNTER += 1
                NO_FACE = MIN_FRAMES    # eliminates shutting off if we see a face
            elif len(faces) == 0:       # no face is found in current frame
                NO_FACE -= 1

            # Draws the rectangle around the face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            # Uses a GUI to display each frame
            cv2.imshow(WINDOW_NAME, img)
            # Wait key to keep the video streaming
            key = cv2.waitKey(1) & 0xFF
            # removes each frame after it's displayed
            rawCapture.truncate(0)

            if FACE_COUNTER == MIN_FACE_COUNT:          # if the face was visible in 15 frames
                FACE_COUNTER = 0 			            # reset the FACE_COUNTER
                print("Found a human")

            # if we have not found a face in MIN_FRAMES, then the camera will
            # shut off and the program will begin looking for motion again.
            if NO_FACE == 0:
                print("False alarm")
                NO_FACE = MIN_FRAMES    # resets to original value
                cv2.destroyAllWindows()  # destroys gui window
                cv2.waitKey(1)          # waits forframes to be destroyed
                cv2.waitKey(1)
                cv2.waitKey(1)
                cv2.waitKey(1)
                break                   # break from inner loop

            if key == ord("q"):		# set EXIT_PROGRAM to 1 for exit
                EXIT_PROGRAM = 1
                break                   # break from inner loop

    camera.close()                      # closes camera to reduce resources.

    if EXIT_PROGRAM == 1:               # if we pressed q, we want to exit.
        break

cv2.destroyAllWindows()                 # destroys gui window
