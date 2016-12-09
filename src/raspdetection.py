from picamera.array import PiRGBArray
from gpiozero import MotionSensor
from twilio.rest import TwilioRestClient
from subprocess import call
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
FILE_NAME = "intruder_%d%s"	        # file name for saving video
VIDEO_COUNT = 1                     # initial count for filename
H264_FORMAT = ".h264"                # h264 format file ext.
MP4_FORMAT = ".mp4"                 # mp4 format file ext.

# Twilio globals
ACCOUNT_SID = " "                   # From Twilio.com/console
AUTH_TOKEN = " "                    # From Twilio.com/console
TWILIO_NUMBER = " "                 # Twilio number used to send SMS
USER_NUMBER = " "                   # Number of user to receive notifications.


def main():
	"""Reads Twilio information from file and starts program. File should be git ignored
	"""
    read_file()
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


def detect_face(camera, rawCapture):
    """Reads each frame from the video and looks for a face. If a face is found
    then we notify the user. If a face is not found then the camera shuts off and
    the script resumes monitoring for motion.

    Keyword arguments:
    camera -- the camera we are receiving video from
    rawCapture -- resizes each frame that we are receiving
    """
    global MIN_FACE_COUNT, MIN_FRAMES, FACE_COUNTER, NO_FACE, EXIT_PROGRAM
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

        draw_rectangle(faces, img)

        cv2.namedWindow(WINDOW_NAME)
        cv2.imshow(WINDOW_NAME, img)
        key = cv2.waitKey(1) & 0xFF
        rawCapture.truncate(0)

        if frame_check() == False:
            return

        if key == ord("q"):
            EXIT_PROGRAM = 1
            return


def draw_rectangle(faces, img):
    """ Draws the box and text around the intruder's face

    Keyword arguments:
    faces -- frames that have faces detected
    img -- the frame itself, this is what we are drawing on.
    """
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


def frame_check():
    """ Sees if we have obtained enough frames to confirm we have a face
    or if we have gone through MIN_FRAMES to determine that it was a false alarm.
    """
    global FACE_COUNTER, NO_FACE, MIN_FRAMES, MIN_FACE_COUNT
    # min frames to say we have a face
    if FACE_COUNTER == MIN_FACE_COUNT:
        FACE_COUNTER = 0
        print("Found a human")
        record_video()
        notify_user()

    # reaching zero implies there's no person
    if NO_FACE == 0:
        print("False alarm")
        NO_FACE = MIN_FRAMES
        cv2.destroyAllWindows()
        # waits for OpenCV's highgui to process
        for i in range(0, 3):
            cv2.waitKey(1)

        return False


def notify_user():
    """ Sends a SMS to a user VIA Twilio's API.
    """
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="An Intruder has been spotted in your space and a video has been recorded",
                                     to=USER_NUMBER,
                                     from_=TWILIO_NUMBER)
    print("User notified!")


def record_video():
	""" Records, saves and converts the video to a MP4 format.
	"""
    global VIDEO_COUNT, camera
    rawFile = FILE_NAME % (VIDEO_COUNT, H264_FORMAT)
    camera.start_recording(rawFile)
    # this is the length of time the camera records
    camera.wait_recording(10)
    camera.stop_recording()
    formatted_file = FILE_NAME % (VIDEO_COUNT, MP4_FORMAT)
    # converts video from .h264 to mp4 for viewing.
    call(["avconv", "-r", "30", "-i", rawFile, "-vcodec", "copy", formatted_file])
    call(["rm", rawFile])
    # allows for multiple video files.
    VIDEO_COUNT += 1
    print("Video saved")

def read_file():
	"""Reads information for Twilio from Text file present on the local machine
	"""
	global TWILIO_NUMBER, USER_NUMBER, ACCOUNT_SID, AUTH_TOKEN
    file = open('twilio.txt', 'r')
    TWILIO_NUMBER = file.readLine()
    USER_NUMBER = file.readLine()
    ACCOUNT_SID = file.readline()
    AUTH_TOKEN = file.readline()

if __name__ == "__main__":
    main()
