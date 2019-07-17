# Countdown capture function
def capture_countdown(delay):
    if delay <= 0:
        print('The countdown number should >= 1')
        print('Please try again ...')
    else:
        countdown = delay
        while countdown >= 1:
            print(countdown)
            sleep(1)
            countdown -= 1
        pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
        camera.capture('../../countdown-pic/' + pic_name + '.jpg')

# ConsoleUI
def consoleUI():
    try:
        user_delay = int(input('Countdown for take a photo: '))
        capture_countdown(user_delay)
    except ValueError:
        print('User input error.')
        print('The countdown number should >= 1.')
        print('Please try again ...')
    finally:
        print('The program ends.')
