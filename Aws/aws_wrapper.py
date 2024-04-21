# print all bucket list which already exits in s3
def show_buckets(s3_obj):
    for bucket in s3_obj.buckets.all():
        print(bucket.name)

# upload file to s3 bucket
def upload_file(s3_obj):
    file_data = open(r'Poonam_cv.pdf','rb')
    s3_obj.Bucket('bucketforpoonam').put_object(Key = 'Poonam rangpariya_cv', Body=file_data)
    file_data.close()
    print("File uploaded successfully")

#list of bucket file
def list_bucket(s3_obj):
    print("Here is all file which you upload in bucket")
    for object in s3_obj.Bucket('bucketforpoonam').objects.all():
        print(object.key)

#create bucket
def create_bucket(s3_obj,bucket_name):
    s3_obj.create_bucket(Bucket=bucket_name)
    print(f"created {bucket_name.upper()} successfully")
