import Auto as autoObj
import Manual as manualObj
# from firebase import Firebase
from picamera import PiCamera
from gpiozero import Button
from gpiozero import MotionSensor
import datetime
import time
import thread
import threading

button = Button(17)
camera = PiCamera()
camera.rotation = 180
pir = MotionSensor(4)
        
def raspi_controller(receiveData):
    global button, camera, pir
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
            if commandName == 'countdown':
                autoObj.recordCountdownObj.consoleUI(camera, datetime, time)
            elif commandName == 'detectIntruder':
                autoObj.recordDetectIntruderObj.record_detect_intruder(pir, datetime, camera, time, 10)
            else:
                print("Don't have " + commandFunc + " command.")
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
        
#try:
#receiveData = {'mode': 'manual-capture-button', 'parameter': ''}
#print('Ready to start new thread !')
#print('Start new thread successfully ...')
#time.sleep(10)
#print('The program exits ...')
#except:
#    print('Error: unable to start thread')

box_data = [
    {'mode': 'manual-capture-button', 'parameter': ''},
    {'mode': 'manual-record-button', 'parameter': ''},
    {'mode': 'auto-capture-countdown', 'parameter': ''},
    {'mode': 'auto-capture-detectIntruder', 'parameter': ''},
    {'mode': 'auto-record-countdown', 'parameter': ''},
    {'mode': 'auto-record-detectIntruder', 'parameter': ''},
    ]

select_index = 0

def run():
    global stop_threads, box_data, select_index
    print('Thread running')
    raspi_controller(box_data[select_index])
        
for i in range(2):
    t1 = threading.Thread(target = run)
    t1.start()
    time.sleep(5)
    t1._Thread__stop()
    select_index += 1
    time.sleep(2)
    
print('Program ends ...') 