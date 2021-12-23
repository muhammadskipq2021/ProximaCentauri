import s3Bucket as s3Bucket
import constants as constant_

def lambda_handler(event,context):
    URLS = s3Bucket.s3_bucket_get_data(constant_.bucket,constant_.file_name)
    print(URLS)