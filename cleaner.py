from boto3.session import Session
import boto3

session = Session(
            aws_access_key_id='''AWS ACCESS KEY''',
            aws_secret_access_key='''AWS SECRET ACCESS KEY''',
            region_name='us-west-2'
        )
s3 = session.client('s3')

resource = boto3.resource('s3') # high-level object-oriented API
my_bucket = resource.Bucket('tf-tech-radar') # put bucket name here

# client = boto3.client('s3')

# all_objects = s3.list_objects(Bucket='tf-tech-radar')

for key in my_bucket.objects.all():
    print(key.key)
    if key.key[-5:] == '.json':
        print('going to delete', key)
        key.delete()

#DELETES everythign in the bucket with the ending ".json"