# import Auto as autoObj
import Manual as manualObj
# from firebase import Firebase
from picamera import PiCamera
from gpiozero import Button
import datetime
import time

'''
{
    'isBusy': False,
    'mode': 'manual-capture-button',
    'parameter': '',

}
'''

button = Button(17)
camera = PiCamera()
camera.rotation = 180

receiveData = {'isBusy': False, 'mode': 'manual-record-button', 'parameter': ''}
if receiveData['isBusy']:
    pass
else:
    modeSplit = receiveData['mode'].split('-')
    commandType = modeSplit[0]
    commandFunc = modeSplit[1]
    commandName = modeSplit[2]
    commandParam = receiveData['parameter']
    if commandType == 'auto':
        # Auto feature
        pass
    elif commandType == 'manual':
        if commandFunc == 'record':
            manualObj.recordButtonObj.record_button(camera, button, datetime, time)
            pass
        elif commandFunc == 'capture':
            manualObj.captureButtonObj.capture_button(camera, button, datetime)
            pass
        else:
            print("Don't have " + commandFunc + " function.")
    else:
        print("Don't have " + commandType + " feature.")