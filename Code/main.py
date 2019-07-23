# Import the necessary module
from gpiozero import MotionSensor
from firebase import firebase
from picamera import PiCamera
from gpiozero import Button
import Manual as manualObj
import Auto as autoObj
import threading
import datetime
import time
import sys
import os

# Initialized global variables
button = Button(17)
camera = PiCamera()
camera.rotation = 180
pir = MotionSensor(4)
raspi_status = None
is_connect_db = False
        
# Implement the feature in raspberry pi
def implement_in_raspi(receiveData):
    global button, camera, pir
    modeSplit = receiveData['mode'].split('-')
    commandType = modeSplit[0]
    commandFunc = modeSplit[1]
    commandName = modeSplit[2]
    commandParam = receiveData['parameter']
    modeName = commandType + commandFunc + commandName
    if commandType == 'auto':
        if commandFunc == 'capture':
            if commandName == 'countdown':
                # auto-capture-countdown
                user_delay = int(commandParam)
                autoObj.captureCountdownObj.capture_countdown(camera, datetime, time, user_delay)
            elif commandName == 'detectIntruder':
                # auto-capture-detectIntruder
                autoObj.captureDetectIntruderObj.capture_detect_intruder(pir, datetime, camera, time)
            else:
                print("Don't have " + modeName + " command.")
        elif commandFunc == 'record':
            if commandName == 'countdown':
                # auto-record-countdown
                paramBox = commandParam.split(',')
                user_delay = int(paramBox[0])
                user_duration = int(paramBox[1])
                autoObj.recordCountdownObj.record_countdown(camera, datetime, time, user_delay, user_duration)
            elif commandName == 'detectIntruder':
                # auto-record-detectIntruder
                user_duration = int(commandParam)
                autoObj.recordDetectIntruderObj.record_detect_intruder(pir, datetime, camera, time, user_duration)
            else:
                print("Don't have " + modeName + " command.")
        else:
            print("Don't have " + modeName + " function.")
    elif commandType == 'manual':
        if commandFunc == 'record':
            # manual-capture-record
            manualObj.recordButtonObj.record_button(camera, button, datetime, time)
        elif commandFunc == 'capture':
            # manual-capture-button
            manualObj.captureButtonObj.capture_button(camera, button, time, datetime)
        else:
            print("Don't have " + modeName + " function.")
    else:
        print("Don't have " + modeName + " feature.")        

# Restart the program
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

# Function for checking the status with the database
def connect_with_database():
    global raspi_status, first_time, firebase, is_connect_db
    firebase = firebase.FirebaseApplication('https://vuejs-http-9ad70.firebaseio.com/', None)
    result = firebase.get('/status', None)
    command_list = list(result.values())
    last_index = len(command_list) - 1
    raspi_status = command_list[last_index]
    is_connect_db = True
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
            print('The current feature has changed. Restart the program.')
            restart_program()

# Running the program
db_thread = threading.Thread(target = connect_with_database)
db_thread.start()
while True:
    if is_connect_db:
        print('Selected feature: ' + raspi_status['mode'])
        implement_in_raspi(raspi_status)
    else:
        time.sleep(1)
        continue