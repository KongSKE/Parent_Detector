from gpiozero import Motionsensor
from picamera import PiCamera
from datetime import datetime

pir = Motionsensor(4)
camera = PiCamera()

while True:
    filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
    pir.wait_for_motion()
    print("Motion Detected!")
    camera.capture('home/pi/video_'+ filename +'.png')
    question = input("Continue Monitoring? (Y)es or (N)o")
    if question == "N" or question == "n":
        print("Camera is closing...")
        camera.close()
