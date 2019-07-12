# from picamera import PiCamera
# from gpiozero import Button
from time import sleep
import datetime

# Initialized
button = Button(17)
camera = PiCamera()
camera.rotation = 180

# Countdown capture function
def capture_countdown(delay):
    if delay <= 0:
        print('The countdown number should >= 1')
        print('Please try again ...')
    else:
        countdown = delay
        while countdown >= 1:
            print(countdown)
            countdown -= 1
        pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
        camera.capture('/home/pi/Parent_Detector/countdown-pic/' + pic_name)
        camera.capture()

# ConsoleUI
try:
    user_delay = int(input('Countdown for take a photo: '))
    capture_countdown(user_delay)
except:
    print('User input error.')
    print('The countdown number should >= 1.')
    print('Please try again ...')
