from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()

while True:
    # filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
    # pir.wait_for_motion()
    # print("Motion Detected!")
    # camera.start_recording(filename +'.h264')
    # pir.wait_for_no_motion
    # camera.stop_recording()
    # question = input("Continue Monitoring? (Y)es or (N)o")
    # if question == "N" or question == "n":
    #     print("Camera is closing...")
    #     camera.close()
