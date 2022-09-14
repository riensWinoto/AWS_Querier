import boto3
import os
import sys

# aws config file path
os.environ['AWS_ACCESS_KEY_ID'] = "yourKeyID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "yourAccessKey"
os.environ['AWS_DEFAULT_REGION'] = "ap-southeast-1"
location = rf"location/and/filename"

rds_client = boto3.client('rds')
desc_response = rds_client.describe_db_instances(
    MaxRecords=100
)

if desc_response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Write rds data to txt file")
    for dbinfo in desc_response['DBInstances']:
        #get db rds info
        file_writer = open(rf"{location}","a")
        file_writer.write(f"{dbinfo['DbiResourceId']},{dbinfo['DBInstanceIdentifier']},{dbinfo['DBInstanceClass']},{dbinfo['EngineVersion']},{dbinfo['StorageType']}\n")
                    
    file_writer.close()                
    print("Finish write rds data")
else:
    print("Failed to fetch data from AWS")
    sys.exit(1)
