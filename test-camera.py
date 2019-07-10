from picamera import PiCamera

camera = PiCamera()

print('The test-camera program starts.')

print('Camera takes a photo name "selfie.png".')

camera.capture('selfie.png')

print('The camera closes.')

camera.close()

print('The program ends.')