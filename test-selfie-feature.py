from picamera import PiCamera
from time import sleep
from gpiozero import Button

# Initialized
button = Button(17)
camera = PiCamera()

# Test the selfie feature
print('The test-selfie-feature starts.')
print('Press the button to take a selfie')
button.wait_for_press()
camera.capture('./testSelfieImage.jpg')
print('Take a selfie!')
camera.close()
print('Close the camera')
print('The program ends.')