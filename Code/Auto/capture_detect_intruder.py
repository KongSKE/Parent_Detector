def capture_detect_intruder(pir, datetime, camera, time):
    print('... capture_detect_intruder starts ...')
    while True:
        try:
            print('Wait for motion ...')
            pir.wait_for_motion()
            pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
            print('Motion detected! Take a picture! ' + pic_name + '.jpg')
            camera.capture('../intruder-pic/' + pic_name + '.jpg')
            time.sleep(1)
        except KeyboardInterrupt:
            print('The capture detect intruder feature ends.')
            break