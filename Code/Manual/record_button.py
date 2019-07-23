# Take the picture by clicking the button.
def record_button(camera, button, datetime, time):
    print('... record_button starts ...')
    while True:
        try:
                camera.start_preview()
                button.wait_for_press()
                video_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
                print('Start recording the video: ' + video_name + '.h264')
                camera.start_recording('../button-video/' + video_name + '.h264')
                time.sleep(3)
                button.wait_for_press()
                camera.stop_recording()
                camera.stop_preview()
                print('Stop recording the video: ' + video_name + '.h264')
                time.sleep(1)
        except KeyboardInterrupt:
                camera.stop_preview()
                break

