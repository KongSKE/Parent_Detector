# Take the picture by clicking the button.
def record_button(camera, button, datetime, time):
    print('... record_button starts ...')
    while True:
        try:
#            camera.start_preview()
            button.wait_for_press()
            video_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
            print('Start recording the video: ' + video_name + '.h264')
#            camera.start_recording('../button-video/' + video_name + '.h264')
            time.sleep(3)
            button.wait_for_press()
#            camera.stop_recording()
            print('Stop recording the video: ' + video_name + '.h264')
#            camera.stop_preview()
#            user_input = raw_input('Do you want to continue ? (y)es : ')
#            if user_input == 'y' or user_input == 'Y':
#                continue
#            print('Exit the record by button feature ...')
#            break
            time.sleep(3)
        except KeyboardInterrupt:
            camera.stop_preview()
            break

