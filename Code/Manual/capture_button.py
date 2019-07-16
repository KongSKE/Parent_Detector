from picamera import PiCamera
from gpiozero import Button
import datetime

# Initialized
def initialized():
    button= Button(17)
    camera = PiCamera()
    camera.rotation = 180

# Take the picture by clicking the button.
def capture_button():
    camera.start_preview()
    while True:
        try:
            button.wait_for_press()
            pic_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
            camera.capture('../../button-pic/' + pic_name + '.jpg')
        except KeyboardInterrupt:
            camera.stop_preview()
            break