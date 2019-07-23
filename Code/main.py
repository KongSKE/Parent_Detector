# Import the necessary module
import Auto as autoObj
import Manual as manualObj
from firebase import firebase
from picamera import PiCamera
from gpiozero import Button
from gpiozero import MotionSensor
import datetime
import time
import threading
import sys
import os
from random import choice

# Initialized global variables
button = Button(17)
camera = PiCamera()
camera.rotation = 180
pir = MotionSensor(4)
raspi_status = None
        
# Implement the feature in raspberry pi
def implement_in_raspi(receiveData):
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

# Restart the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Function for checking the status with the database
def connect_with_database():
    global raspi_status, first_time, firebase
    firebase = firebase.FirebaseApplication('https://vuejs-http-9ad70.firebaseio.com/', None)
    result = firebase.get('/status', None)
    command_list = list(result.values())
    last_index = len(command_list) - 1
    raspi_status = command_list[last_index]
    while True:
        result_2 = firebase.get('/status', None)
        command_list_2 = list(result_2.values())
        last_index_2 = len(command_list_2) - 1
        raspi_status_2 = command_list_2[last_index_2]
        if raspi_status == raspi_status_2:
            time.sleep(3)
            continue
        else:
            camera.close()
            print('User changes the feature. Restart the program.')
            restart_program()

# Running the program
db_thread = threading.Thread(target = connect_with_database)
db_thread.start()
time.sleep(1)
print('Selected feature: ' + raspi_status['mode'])
implement_in_raspi(raspi_status)

# Demo
# select_index = choice([0,1])
# box_data = [
#     {'mode': 'manual-capture-button', 'parameter': ''},
#     {'mode': 'manual-record-button', 'parameter': ''},
#     {'mode': 'auto-capture-countdown', 'parameter': ''},
#     {'mode': 'auto-capture-detectIntruder', 'parameter': ''},
#     {'mode': 'auto-record-countdown', 'parameter': ''},
#     {'mode': 'auto-record-detectIntruder', 'parameter': ''},
#     ]
# db_thread = threading.Thread(target = connect_with_database)
# db_thread.start()
# time.sleep(2)
# print('Selected: ' + str(select_index))
# implement_in_raspi(box_data[select_index])

print('Program ends ...') 