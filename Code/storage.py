from google.cloud import storage
import os
import pyrebase

''' Global variable '''
bucket_name = 'vuejs-http-9ad70.appspot.com'

''' Setup '''
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'GOOGLE_APPLICATION_CREDENTIALS.json'
storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)

''' Create bucket '''
def create_bucket(bucket_name):
    global storage_client
    bucket = storage_client.create_bucket(bucket_name)
    print('Bucket {} created'.format(bucket_name))

''' Uploads a file to the bucket. '''
def upload_blob(source_file_name, destination_blob_name):
    global bucket
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print('File {} uploaded to {}'.format(source_file_name, destination_blob_name))
    
''' Download a file from the bucket'''
def download_blob(source_blob_name, destination_file_name):
    global bucket
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print('File {} downloaded to {}'.format(source_blob_name, destination_file_name))
    
    
''' List buckets & items '''
def list_buckets_and_items():
    global storage_client
    buckets = storage_client.list_buckets()
    for bucket in buckets:
        print('Bucket name: ' + bucket.name)
        for item in bucket.list_blobs():
            print('\t' + item.name)