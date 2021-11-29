'''
An AWS Lambda function that triggers every time a .zip file is put in a storage bucket
unzipping to the target bucket. This doesn't seem to work as the phase two file is not being
recognised as a zip file.
'''

import json
import boto3
from io import BytesIO
import zipfile

def lambda_handler(event, context): 
    s3 = boto3.resource('s3')
    source_bucket = 'goodcropbadcropzip'
    target_bucket = 'goodcropbadcrop'
    my_bucket = s3.Bucket(source_bucket)
    
    for file in my_bucket.objects.all():
        if(str(file.key).endswith('.zip')):
            zip_object = s3.Object(bucket_name = source_bucket, key = file.key)
            buffer = BytesIO(zip_object.get()['Body'].read(amt=200))
            
            z = zipfile.ZipFile(buffer)
            for filename in z.namelist():
                file_info = z.getinfo(filename)
                s3.meta.client.upload_fileobj(
                        z.open(filename),
                        Bucket = target_bucket,
                        key = f'{filename}'
                        ) 
        else:
            print(' '.join(file.key, 'is not a zip file'))
