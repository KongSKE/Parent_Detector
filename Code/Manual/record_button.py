# Take the picture by clicking the button.
def record_button(camera, button, datetime, time):
    while True:
        try:
#            camera.start_preview()
            button.wait_for_press()
            video_name = '../button-video/' + str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_') + '.h264'
            camera.start_recording(video_name)
            time.sleep(3)
            button.wait_for_press()
            camera.stop_recording()
#            camera.stop_preview()
            user_input = raw_input('Do you want to continue ? (y)es : ')
            if user_input == 'y' or user_input == 'Y':
                continue
            print('Exit the record by button feature ...')
            break
        except KeyboardInterrupt:
            camera.stop_preview()
            break

