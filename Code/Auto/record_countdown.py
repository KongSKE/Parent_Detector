def record_countdown(camera, datetime, time, delay, duration):
    if delay <= 0:
        print('The countdown number should >= 1')
        print('Please try again ...')
    else:
        countdown = delay
        while countdown >= 1:
            print(countdown)
            time.sleep(1)
            countdown -= 1
        print('Start recording ...')
        video_name = '../countdown-video/' + str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_') + '.h264'
        camera.start_recording(video_name)
        time.sleep(duration)
        camera.stop_recording()

def consoleUI(camera, datetime, time):
    while True:
        try:
            user_delay = int(input('Countdown for record a video : '))
            user_duration = int(input('Duration for record a video : '))
            record_countdown(camera, datetime, time, user_delay, user_duration)
            user_input = str(raw_input('Do you want to continue ? (Y)es : '))
            if user_input == 'y' or user_input == 'Y':
                continue
            break
        except ValueError:
            print('User input error.')
            print('The countdown number should >= 1.')
            print('Please try again ...')
    print('The record countdown program ends.')