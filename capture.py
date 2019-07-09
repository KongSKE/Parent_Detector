from picamera import Picamera
from time import sleep
from gpiozero import Button

'Take a photo by button clicking'

button= Button(17)
camera = Picamera()

camera.rotation = 180
camera.start_preview()
# button.wait_for_press()
# sleep(3)
# camera.capture('./image.jpg')
# camera.stop_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break