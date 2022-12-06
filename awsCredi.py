
import boto3
def myAwsCred():
dynamodb = boto3.resource('dynamodb',aws_access_key_id="User your access key", aws_secret_access_key="use your secret access key", region_name="us-east-2",endpoint_url="http://localhost:8000")
return dynamodb
