# Countdown capture function
def capture_countdown(camera, datetime, time, delay):
    if delay <= 0:
        print('The countdown number should >= 1')
        print('Please try again ...')
    else:
        countdown = delay
        while countdown >= 1:
            print(countdown)
            time.sleep(1)
            countdown -= 1
        pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
        camera.capture('../countdown-pic/' + pic_name + '.jpg')

# ConsoleUI
def consoleUI(camera, datetime, time):
    while True:
        try:
            user_delay = int(input('Countdown for take a photo: '))
            capture_countdown(camera, datetime, time, user_delay)
            user_input = str(raw_input('Do you want to continue ? (Y)es : '))
            if user_input == 'y' or user_input == 'Y':
                continue
            break
        except ValueError:
            print('User input error.')
            print('The countdown number should >= 1.')
            print('Please try again ...')
    print('The capture countdown program ends.')