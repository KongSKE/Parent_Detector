def record_countdown(camera, datetime, time, delay, duration):
    print('... record_countdown starts ...')
    while True:
        if delay <= 0:
            print('The countdown number should >= 1')
            print('Please try again ...')
            break
        else:
            print('The record countdown feature will start in ...')
            countdown = delay
            while countdown >= 1:
                print(countdown)
                time.sleep(1)
                countdown -= 1
            video_name = '../countdown-video/' + str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_') + '.h264'
            print('Start recording ...' + video_name + '.h264')
            camera.start_recording(video_name)
            time.sleep(duration)
            print('Stop recording ...' + video_name + '.h264')
            camera.stop_recording()
            time.sleep(1)