import boto3
from botocore.exceptions import ClientError
import os

# aws config file path
os.environ['AWS_ACCESS_KEY_ID'] = "yourKeyID"
os.environ['AWS_SECRET_ACCESS_KEY'] = "yourAccessKey"
os.environ['AWS_DEFAULT_REGION'] = "ap-southeast-1"
user_name = "dummy_riens"
arr_access_key_id = []
arr_policy_name = []
arr_attached_policy_name = []
arr_groups_for_user = []

iam_client = boto3.client('iam')

#delete login profile
print("Try to delete login profile")
try:
    delete_login_profile_resp = iam_client.delete_login_profile(
        UserName=user_name
    )
    if delete_login_profile_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
        print("Login profile have been deleted")
    else: 
        print("Failed to delete login profile")
except ClientError as e:
    print(e)


#list access key
print("\nTry to listing access key")
list_access_key_resp = iam_client.list_access_keys(
    UserName=user_name
)
if list_access_key_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Listing access key:")
    if len(list_access_key_resp['AccessKeyMetadata']) == 0:
        print("No access key")
    else:
        for each_list_access_key in list_access_key_resp['AccessKeyMetadata']:
            arr_access_key_id.append(each_list_access_key['AccessKeyId'])
            print(each_list_access_key['AccessKeyId'])
else:
    print("Failed to listing access key")

#delete access key
print("\nTry to delete access key")
if len(arr_access_key_id) == 0:
    print("No access key")
else:
    for each_access_key_id in arr_access_key_id:    
        delete_access_key_resp = iam_client.delete_access_key(
            UserName=user_name,
            AccessKeyId=each_access_key_id
        )
        if delete_access_key_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"{each_access_key_id} have been deleted")
        else:
            print(f"Failed to delete {each_access_key_id} access key")

#list user polices
print("\nTry to listing user policies")
list_user_policies_resp = iam_client.list_user_policies(
    UserName=user_name
)
if list_user_policies_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
    if len(list_user_policies_resp['PolicyNames']) == 0:
        print("No inline policies")
    else:
        print("Listing user policies:")
        for each_list_user_policies in list_user_policies_resp['PolicyNames']:
            arr_policy_name.append(each_list_user_policies)
            print(each_list_user_policies)
else:
    print("Failed to listing user policies")
       
#delete user policies
print("\nTry to delete user policies")
if len(arr_policy_name) == 0:
    print("No inline policies")
else:
    for each_policy_name in arr_policy_name:
        delete_user_policy_resp = iam_client.delete_user_policy(
            UserName=user_name,
            PolicyName=each_policy_name
        )
        if delete_user_policy_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"{each_policy_name} have been deleted from user")
        else:
            print(f"Failed to delete {each_policy_name} from user")

#list attached user policies
print("\nTry to listing attached user policies")
list_attached_user_policies_resp = iam_client.list_attached_user_policies(
    UserName=user_name
)
if list_attached_user_policies_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
    if len(list_attached_user_policies_resp['AttachedPolicies']) == 0:
        print("No attached user policies")
    else:
        print("Listing attached user policies:")
        for each_list_attached_user_policies in list_attached_user_policies_resp['AttachedPolicies']:
            arr_attached_policy_name.append(each_list_attached_user_policies['PolicyArn'])
            print(each_list_attached_user_policies['PolicyArn'])
else:
    print("Failed to listing attached user policies")

#delete attached user policies
print("\nTry to delete attached user policies")
if len(arr_attached_policy_name) == 0:
    print("No attached user policies")
else:
    for each_attached_policy_name in arr_attached_policy_name:
        detach_user_policy_resp = iam_client.detach_user_policy(
            UserName=user_name,
            PolicyArn=each_attached_policy_name
        )
        if detach_user_policy_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"{each_attached_policy_name} have been deleted from user")
        else:
            print(f"Failed to delete {each_attached_policy_name} from user")

#listing groups for user
print("\nTry to listing group for user")
list_groups_for_user_resp = iam_client.list_groups_for_user(
    UserName=user_name
)
if list_groups_for_user_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
    if len(list_groups_for_user_resp['Groups']) == 0:
        print("No groups for user")
    else:
        print("Listing groups for user:")
        for each_list_groups_for_user in list_groups_for_user_resp['Groups']:
            arr_groups_for_user.append(each_list_groups_for_user['GroupName'])
            print(each_list_groups_for_user['GroupName'])
else:
    print("Failed to listing groups for user")

#remove user from group
print("\nTry to delete groups for user")
if len(arr_groups_for_user) == 0:
    print("No groups for user")
else:
    for each_groups_for_user in arr_groups_for_user:
        remove_user_from_group_resp = iam_client.remove_user_from_group(
            UserName=user_name,
            GroupName=each_groups_for_user
        )
        if remove_user_from_group_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"{each_groups_for_user} have been deleted from user")
        else:
            print(f"Failed to delete {each_groups_for_user} from user")

#delete user
print("\nTry to delete user")
delete_user_resp = iam_client.delete_user(
    UserName=user_name
)
if delete_user_resp['ResponseMetadata']['HTTPStatusCode'] == 200:
    print(f"{user_name} have been deleted from IAM")
else:
    print(f"Failed to delete {user_name} form IAM")
