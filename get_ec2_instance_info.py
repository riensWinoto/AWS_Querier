import boto3
import os

# aws config file path
os.environ['AWS_ACCESS_KEY_ID'] = "yourKeyID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "yourAccessKey"
os.environ['AWS_DEFAULT_REGION'] = "ap-southeast-1"
location = rf"location/and/filename"

# general variable
counterx = []
countery = []

ec2_client = boto3.client('ec2')
desc_response = ec2_client.describe_instances(
    Filters=[
        {
        'Name' : 'architecture',
        'Values': ['x86_64',
                   ]
        },
    ],
    MaxResults=1000
)

for index in desc_response['Reservations']:
    #get instance id
    for idx in index['Instances']:
        counterx.append(f"{idx['InstanceId']}")

        #get instance name
        for tag_name in idx['Tags']:
            if tag_name['Key'] == 'Name':
                countery.append(f"{idx['InstanceId']}")
                file_writer = open(rf"{location}","a")
                file_writer.write(f"{idx['InstanceId']},{tag_name['Value']},{idx['InstanceType']}\n")
                
file_writer.close()                
print(f"total instance: {len(counterx)}")
print(f"total instance with names / non jenkins worker: {len(countery)}")
