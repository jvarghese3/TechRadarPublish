
#This only records messages since this starts being run on a slack channel.
#  I am confident that there is a way to get all of them as I'd done it before,
# so it doesnt take much adjustment. It seems to be an issue with the Slack API
# because that's the only thing that records stuff from the channel
# But it shouldn't be too hard to fix

import os
from slackclient import SlackClient
import uuid
from utiler import save_to_local_json
import hashlib

#right click on channel to get the name at te end of the URL
slack_token = os.environ.get("'Slack token'") #CONFIDENTIAL
sc = SlackClient("Slack Token") #KEEP PRIVATE

sc.api_call(
    "chat.postMessage",
    channel="__", #change channel name here
    text="Got the history!" #LEt's you knwo that the history was acquired

)

convo = sc.api_call(
    "conversations.history",
    channel="  ", #for the channel name here, you need to copy the URL
    #and use the ending part which will probably start with a C
)


from boto3.session import Session

session = Session(
            aws_access_key_id='''AWS ACCESS KEY''',
            aws_secret_access_key='''AWS SECRET ACCESS KEY''',
            region_name='us-west-2'
        )
s3 = session.client('s3')

#The flatten values function is meant to isolate each message so they can all be
# ashed if the messages happened to be in the same file,
# which is how the Slack API delivers it
'''
def flattenValues(mapObj):
    return "".join(
        map(str, mapObj.values())
        #converts each value to strings
    )
    #this is to be used if all multiple messages are in a single file
'''

def createHashableString(mapObj):
    if 'username' in mapObj.keys():
        return mapObj['username'] + mapObj['ts']
    elif 'user' in mapObj:
        return mapObj['user'] + mapObj['ts']
    else:
        raise Exception('User field not found')


status = convo["ok"]
if status == True:
    # save each msg to S3

    msgs = convo["messages"]
    for msg in msgs:
        # for each msg, create a local temp file
        encoded = bytearray(createHashableString(msg), 'utf-8')
        #needed to encode string as bytearray
        #msg is a Python dictionary
        uname =  (hashlib.md5(encoded).hexdigest())
        #saves each msg to a hash using MD5

        print (uname)
        save_to_local_json("%s.tmp" % uname, msg)

        # create hash

        # upload to S3 as uuid.json
        s3.upload_file("./data/%s.tmp" % uname, '''Bucket Name''', "%s.json" % uname)
        os.remove("./data/%s.tmp" % uname)
else:
    print ("Error while pulling data from channel. Saving to local file")
    save_to_local_json('tech_radar_all.json', convo)


import boto3
from boto3.session import Session
import hashlib

client = boto3.client('s3')

resource = boto3.resource('s3') # high-level object-oriented API
my_bucket = resource.Bucket(' ') # put bucket name here


all_objects = s3.list_objects(Bucket='''Bucket Name''')


counts={}
for item in all_objects['Contents']:
    uname = item['Key']
    if uname not in counts.keys():
        counts[uname] = 1
    else:
        counts[uname] += 1

#checks for duplicates and tells you what they are
#AWS already replaces duplicates for you
duplicates=[k for k, count in counts.items() if count > 1]
print (duplicates)

