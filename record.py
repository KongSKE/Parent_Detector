from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
filename = "intruder.h264"

while true:
    pir.wait_for_motion()
    print("Motion Detected")
    camera.start_recording(filename)
    pir.wait_for_no_motion
    camera.stop_recording()
    question = input("Do you wanna continue monitoring? (Y)es or (N)o: ")
    if question == 'n':
        break
    
