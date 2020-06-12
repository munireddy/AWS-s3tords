import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket_list = []
    
    for bucket in s3.buckets.all():
        print(bucket.name)
        bucket1 = s3.Bucket(bucket.name)
        for obj in bucket1.objects.all():
            print(obj.key)
        bucket_list.append(bucket.name)
        print ('!!!!!!!!!!!!!!!!!!!!!!!!!!1 NEXT BUCKET !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    
    
    return {
        'statusCode': 200,
        'body': bucket_list
    }
