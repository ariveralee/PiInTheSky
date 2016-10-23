from gpiozero import MotionSensor
from picamera import picamera

camera = PiCamera()
motionSensor = MotionSensor(4) #Output to pin 4
while True:
	motionSensor.wait_for_motion()
	camera.start_preview()
	motionSensor.wait_for_no_motion()
	camera.stop_preview()

