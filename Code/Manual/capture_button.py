# Take the picture by clicking the button.
def capture_button(camera, button, time, datetime, bucket, os):
    print('... capture_button starts ...')
    while True:
        try:
                # Create image file
                camera.start_preview()
                button.wait_for_press()
                pic_name = str(datetime.datetime.now())[:19:].replace(':', '-').replace(' ','_')
                camera.capture('../button-pic/' + pic_name + '.jpg')
                camera.stop_preview()
                print('Take the picture: ' + pic_name + '.jpg')

                # Upload into firebase storage
                source_file_name = '../button-pic/' + pic_name + '.jpg'
                destination_blob_name = 'button-pic/' + pic_name + '.jpg'
                blob = bucket.blob(destination_blob_name)
                blob.upload_from_filename(source_file_name)
                print('File {} uploaded to {}'.format(source_file_name, destination_blob_name))
                
                # Delete uploaded file
                os.remove('../button-pic/' + pic_name + '.jpg')

                time.sleep(1)
        except KeyboardInterrupt:
                camera.stop_preview()
                break   
