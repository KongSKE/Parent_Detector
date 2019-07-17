# Take the picture by clicking the button.
def capture_button():
    global camera, button
    camera.start_preview()
    while True:
        try:
            button.wait_for_press()
            pic_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
            camera.capture('../../button-pic/' + pic_name + '.jpg')
        except KeyboardInterrupt:
            camera.stop_preview()
            break