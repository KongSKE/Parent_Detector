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
import multiprocessing
import sys
import os
from random import choice

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
            manualObj.captureButtonObj.capture_button(camera, button, time, datetime)
        else:
            print("Don't have " + commandFunc + " function.")
    else:
        print("Don't have " + commandType + " feature.")        

box_data = [
    {'mode': 'manual-capture-button', 'parameter': ''},
    {'mode': 'manual-record-button', 'parameter': ''},
    {'mode': 'auto-capture-countdown', 'parameter': ''},
    {'mode': 'auto-capture-detectIntruder', 'parameter': ''},
    {'mode': 'auto-record-countdown', 'parameter': ''},
    {'mode': 'auto-record-detectIntruder', 'parameter': ''},
    ]

select_index = choice([0,1])

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def run():
    while True:
        user_input = str(raw_input('numbers 0 - 5 : '))
        if select_index == int(user_input):
            continue
        else:
#            camera.stop_preview()
#            camera.stop_recording()
            print('Restart .')
            camera.close()
            restart_program()
    
t1 = threading.Thread(target = run)
t1.start()
time.sleep(2)
print('Selected: ' + str(select_index))
raspi_controller(box_data[select_index])


    
print('Program ends ...') 