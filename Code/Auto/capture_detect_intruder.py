def capture_detect_intruder(pir, datetime, camera, time):
    while True:
        try:
            pir.wait_for_motion()
            pic_name = str(datetime.datetime.now())[:19:].replace(':', '.')
            print('Motion detected! Take a picture! ' + pic_name + '.jpg')
            camera.capture('../intruder-pic/' + pic_name + '.jpg')
#            print('The camera can be use again in ...')
#            countdown = 3
#            while countdown >= 1:
#                print(countdown)
#                time.sleep(1)
#                countdown -= 1
        except KeyboardInterrupt:
            print('The capture detect intruder feature ends.')
            break