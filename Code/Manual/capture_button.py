# Take the picture by clicking the button.
def capture_button(camera, button, time, datetime):
    print('... capture_button starts ...')
    while True:
        try:
                camera.start_preview()
                button.wait_for_press()
                pic_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
                camera.capture('../button-pic/' + pic_name + '.jpg')
                camera.stop_preview()
                print('Take the picture: ' + pic_name + '.jpg')
                time.sleep(1)
        except KeyboardInterrupt:
                camera.stop_preview()
                break   
