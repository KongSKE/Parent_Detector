import Auto as autoObj
import Manual as manualObj
# from firebase import Firebase
from picamera import PiCamera
from gpiozero import Button
from gpiozero import MotionSensor
import datetime
import time

'''
{
    'mode': 'manual-capture-button',
    'parameter': '',

}
'''

button = Button(17)
camera = PiCamera()
camera.rotation = 180
pir = MotionSensor(4)

receiveData = {'mode': 'auto-capture-detectIntruder', 'parameter': ''}

modeSplit = receiveData['mode'].split('-')
commandType = modeSplit[0]
commandFunc = modeSplit[1]
commandName = modeSplit[2]
commandParam = receiveData['parameter']
if commandType == 'auto':
    if commandFunc == 'capture':
        if commandName == 'countdown':
            autoObj.captureCountdownObj.consoleUI(camera, datetime, time)
        elif commandName == 'detectIntruder':
            autoObj.captureDetectIntruderObj.capture_detect_intruder(pir, datetime, camera, time)
        else:
            print("Don't have " + commandFunc + " command.")
    elif commandFunc == 'record':
        pass
    else:
        print("Don't have " + commandFunc + " function.")
elif commandType == 'manual':
    if commandFunc == 'record':
        manualObj.recordButtonObj.record_button(camera, button, datetime, time)
    elif commandFunc == 'capture':
        manualObj.captureButtonObj.capture_button(camera, button, datetime)
    else:
        print("Don't have " + commandFunc + " function.")
else:
    print("Don't have " + commandType + " feature.")