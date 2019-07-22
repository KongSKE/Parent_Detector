def record_detect_intruder(pir, datetime, camera, time, duration):
    while True:
        try:
            print('Wait for motion ...')
            pir.wait_for_motion()
            video_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
            print('Motion detected! Record the video! ' + video_name + '.h264')
            camera.start_recording('../intruder-video/' + video_name + '.h264')
            time.sleep(duration)
            camera.stop_recording()
            break
#            print('The camera can be use again in ...')
#            countdown = 3
#            while countdown >= 1:
#                print(countdown)
#                time.sleep(1)
#                countdown -= 1
        except KeyboardInterrupt:
            print('The capture detect intruder feature ends.')
            break
