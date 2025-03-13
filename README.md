# python_boto3
Automate creation of EC2-tags upon instance creation with the name of the creator and instance id as EC2 Key Value . This lets admins and SRE to keep track of who created a resource by having this automation in place.

Steps:

1. Setup Cloud trail to capture AWS events
    - Create a Cloudwatch log for it to get notified when activity occurs

2. Create AWS eventbrige to trigger our python lambda function when a specific event pattern meets. For example when RunInstance eventype is tri.gered. When that occurs the idea is that our lambda function create a tag on the resource created with the name of the creator( the function collects the Unsername and instance Id from the event data funtion and tags the resource with those values )
    
    3. Create an EC2 instance and check whether the instance is tagged properly

    - check cloudwatch logs for any errors or anomalities
    - The lanbda function will obviosly lack proper IaM permission to do any activity against EC2 like we have specified - create_tags.
    - therefore add ec2:CreateTags policy to the existing lambdaexecution IAM role created automatically at the time of creating the lambda funtion

    NOTE: This code  only inside AWS lambda function. This can be also done from our local devlopment machine once all required prerequisites are in place such as 
    - Boto3
    - Python
    - AWS credentials
