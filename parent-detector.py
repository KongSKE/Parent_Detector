from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()

# Code for take a photo
'''
from picamera import PiCamera
camera = PiCamera()
camera.capture('home/pi/selfie.png')
camera.close()
'''

# Code for recording the video file
'''
from datetime import datetime
from gpiozero import MotionSensor
from picamera import PiCamera
pir = MotionSensor(4)
camera = PiCamera()
while True:
    filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
    pir.wait_for_motion()
    print('Motion detected!')
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
'''

while True:
    pir.wait_for_motion()
    print('Motion detected!')
    camera.start_preview()
    pir.wait_for_no_motion()
    camera.stop_preview()