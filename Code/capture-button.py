from picamera import PiCamera
from gpiozero import Button
import datetime

# Initialized
button= Button(17)
camera = PiCamera()
camera.rotation = 180

# Take the picture by clicking the button.
camera.start_preview()
while True:
    try:
        button.wait_for_press()
        pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
        camera.capture('/home/pi/Parent_Detector/button-pic/' + pic_name)
    except KeyboardInterrupt:
        camera.stop_preview()
        break