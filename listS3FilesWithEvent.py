import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket_list = []
    print(event['Name'])
    if (event['Name']) == 'Muni':
        bucket_list.append('You are author of the code')
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket_list.append(bucket.name)
    
    
    return {
        'statusCode': 200,
        'body': bucket_list
    }
