import boto3
import botocore
import csv

BUCKET_NAME = 'munis3tordsbucket' # replace with your bucket name
KEY = 'muni123.csv' # replace with your object key

s3 = boto3.resource('s3')

try:
    s3.Bucket(BUCKET_NAME).download_file(KEY, KEY)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise
#------------------ Print the contents of the file -------
ifh = open(KEY, 'r')
csv_data = csv.reader(ifh, delimiter=',')
print (csv_data)
for row in csv_data:
    #cursor.bindarraysize = 1
    #cursor.setinputsizes(int, 20, float)
    print("iB4 insert")
    print(row)
    #cursor.execute('insert into muni4 (srollno, name1, efees) VALUES(:1, :2, :3)', row)
    print("AF insert")
