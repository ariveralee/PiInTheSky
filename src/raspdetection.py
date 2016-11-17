from picamera.array import PiRGBArray
from gpiozero import MotionSensor
from twilio.rest import TwilioRestClient
import picamera
import numpy as np
import cv2
import time

# Loads haar cascades for facial detection reference
face_cascade = cv2.CascadeClassifier(
    '/home/pi/opencv-3.1.0/data/lbpcascades/lbpcascade_frontalface.xml')

MIN_FACE_COUNT = 15                 # min frames before we detected a person
MIN_FRAMES = 60                     # frames needed w.o a face before we stop searching
FACE_COUNTER = 0                    # increments for each frame a face is found
NO_FACE = MIN_FRAMES                # when zero, shuts off camera.
EXIT_PROGRAM = 0                    # When 1, program quits
WINDOW_NAME = "Security feed"       # Window name for feed
MOTION_SENSOR = MotionSensor(4)     # motion sensor sends output to pin 4

# Twilio globals
# Account SID from www.twilio.com/console
ACCOUNT_SID = "account"
# Auth Token from www.twilio.com/console
AUTH_TOKEN = "auth_token"
TWILIO_NUMBER = "+12672744736"      # Twilio number used to send SMS
USER_NUMBER = "+12673998007"        # Number of user to receive notifications.


def main():
    detect_motion()
    print("Exiting Program")


def detect_motion():
    """Pauses the script until motion has been detected VIA the PIR sensor.
    """
    while True:
        print("Scanning for motion")
        MOTION_SENSOR.wait_for_motion()  # pauses program until motion is detected

        if MOTION_SENSOR.motion_detected == True:
            print("Motion detected!")
            initialize_camera()

        camera.close()

        if EXIT_PROGRAM == 1:
            cv2.destroyAllWindows()
            return


def initialize_camera():
    """turns on camera for detection of a face in video feed
    """
    global camera
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 30
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.1)
    detect_face(camera, rawCapture)


def notify_user():
    """ Sends a SMS to a user VIA Twilio's API.
    """
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="An Intruder has been spotted in your space",
                                     to=USER_NUMBER,
                                     from_=TWILIO_NUMBER)
    print("User notified!")


def detect_face(camera, rawCapture):
    """Reads each frame from the video and looks for a face. If a face is found
    then we notify the user. If a face is not found then the camera shuts off and
    the script resumes monitoring for motion.

    Keyword arguments:
    camera -- the camera we are receiving video from
    rawCapture -- resizes each frame that we are receiving
    """
    global MIN_FACE_COUNT, MIN_FRAMES, FACE_COUNTER, NO_FACE, EXIT_PROGRAM, WINDOW_NAME, MOTION_SENSOR
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        img = frame.array
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.5, 3)

        # greater than 0 means a face is present
        if len(faces) != 0:
            FACE_COUNTER += 1
            NO_FACE = MIN_FRAMES
        # no face is present in current frame
        elif len(faces) == 0:
            NO_FACE -= 1

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.namedWindow(WINDOW_NAME)
        cv2.imshow(WINDOW_NAME, img)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)

        # min frames to say we have a face
        if FACE_COUNTER == MIN_FACE_COUNT:
            FACE_COUNTER = 0
            print("Found a human")
            notify_user()

        # reaching zero implies there's no person
        if NO_FACE == 0:
            print("False alarm")
            NO_FACE = MIN_FRAMES
            cv2.destroyAllWindows()
            # waits for OpenCV's highgui to process
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            cv2.waitKey(1)
            return

        if key == ord("q"):
            EXIT_PROGRAM = 1
            return

main()
