import boto3
import os
import sys

# aws config file path
os.environ['AWS_ACCESS_KEY_ID'] = "yourKeyID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "yourAccessKey"
os.environ['AWS_DEFAULT_REGION'] = "ap-southeast-1"

iam_client = boto3.client('iam')
list_user_response = iam_client.list_users(
    MaxItems=100
)

if list_user_response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Retrieve IAM users")
    for iam_users in list_user_response['Users']:
        print(f"User ID: {iam_users['UserId']}")
        print(f"Username: {iam_users['UserName']}\n")
    print("All IAM users have been retrieved")
else:
    print("Failed to fetch data from AWS")
    sys.exit(1)

