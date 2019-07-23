def record_detect_intruder(pir, datetime, camera, time, duration):
    print('... record_detect_intruder starts ...')
    while True:
        try:
            print('Wait for motion ...')
            pir.wait_for_motion()
            video_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
            print('Motion detected! Record the video! ' + video_name + '.h264')
            print('Start recording ...' + video_name + '.h264')
            camera.start_recording('../intruder-video/' + video_name + '.h264')
            time.sleep(duration)
            camera.stop_recording()
            print('Start recording ...' + video_name + '.h264')
            time.sleep(1)
        except KeyboardInterrupt:
            print('The capture detect intruder feature ends.')
            break
