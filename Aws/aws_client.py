import boto3
from aws_wrapper import show_buckets,upload_file,list_bucket,create_bucket


s3_obj = boto3.resource('s3')
show_buckets(s3_obj)
upload_file(s3_obj)
list_bucket(s3_obj)
create_bucket(s3_obj,'uppercreatebucket')
