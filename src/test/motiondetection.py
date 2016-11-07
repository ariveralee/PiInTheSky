from gpiozero import MotionSensor

pir = MotionSensor(4)           # Motion sensor sends output to pin 4
while True;
    if pir.motion_detected:
        print("Detected motion!")