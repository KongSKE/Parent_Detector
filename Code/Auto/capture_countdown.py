def capture_countdown(camera, datetime, time, delay):
    print('... capture_countdown starts ...')
    while True:
        if delay <= 0:
            print('The countdown number should >= 1')
            print('Please try again ...')
            break
        else:
            print('The capture countdown feature will start in ...')
            countdown = delay
            while countdown >= 1:
                print(countdown)
                time.sleep(1)
                countdown -= 1
            pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
            camera.capture('../countdown-pic/' + pic_name + '.jpg')
            print('Take the picture! ' + pic_name + '.jpg')
            time.sleep(1)