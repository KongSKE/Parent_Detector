# import Auto as autoObj
import Manual as manualObj
# from firebase import Firebase
import time
from picamera import PiCamera
from gpiozero import Button
import datetime

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

receiveData = {'isBusy': False, 'mode': 'manual-capture-button', 'parameter': ''}
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
        if commandFunc == 'capture':
            manualObj.captureButtonObj.initialized()
            manualObj.captureButtonObj.capture_button()
        else:
            # Record manual feature
            pass
    else:
        # Error
        pass