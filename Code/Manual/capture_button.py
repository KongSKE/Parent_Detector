# Take the picture by clicking the button.
def capture_button(camera, button, datetime):
    print('... capture_button starts ...')
    while True:
        try:
#            camera.start_preview()
            button.wait_for_press()
            pic_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
            camera.capture('../button-pic/' + pic_name + '.jpg')
#            camera.stop_preview()
            user_input = raw_input('Do you want to continue ? (y)es : ')
            if user_input == 'y' or user_input == 'Y':
                continue
            print('Exit the capture by button feature ...')
            break
        except KeyboardInterrupt:
            camera.stop_preview()
            break
    print('... capture_button ends ...')
