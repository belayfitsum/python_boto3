import json
import boto3

ec2 = boto3.client('ec2')

# before doing any action, get instance information with the event data
# to get userID information of the user who created the instances
# collect UserID information.
def lambda_handler(event, context):
    print(event)

    user = event['detail']['userIdentity']['userName']

    instanceID = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']

    ec2.create_tags(
        Resources=[instanceID],
        Tags=[
            {
                'Key': 'Owner',
                'Value': user
            },
        ]
    )

    return