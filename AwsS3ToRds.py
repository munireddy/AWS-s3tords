import cx_Oracle
import boto3
import csv
import uuid
import json

client = boto3.client("s3")
# Create a table in Oracle database
try:
    print ( "Start of the program")
    bucket_name = 'munis3tordsbucket'
    s3_file_name = 'muni123.csv'
    res = client.get_object(Bucket=bucket_name, Key=s3_file_name)
    #download_path = '/home/ubuntu/db/'.format(s3_file_name)
    download_path = '/tmp/{}{}'.format(uuid.uuid4(), s3_file_name)
    client.download_file(bucket_name,s3_file_name,download_path)
    csv_data = csv.reader(download_path)
    print ( "End of S3 download")

    #dsn_tns = cx_Oracle.makedsn('czoradb011.cnsafvgtfe5w.us-east-2.rds.amazonaws.com', '152', service_name='ORCL')
    dsn_tns = cx_Oracle.makedsn("czoradb011.cnsafvgtfe5w.us-east-2.rds.amazonaws.com", "1521", "ORCL")

    #con = cx_Oracle.connect('admin/cZenix2020@czoradb011.cnsafvgtfe5w.us-east-2.rds.amazonaws.com')
    con = cx_Oracle.connect(user=r'admin', password='cZenix2020', dsn=dsn_tns)
    #con = cx_Oracle.connect('admin/cZenix2020@czoradb011.cnsafvgtfe5w.us-east-2.rds.amazonaws.com')
    print ( "After DB connect")

    # Now execute the sqlquery
    cursor = con.cursor()
    print ( "After cursor")
    ifh = open(download_path, 'r')
    csv_data = csv.reader(ifh, delimiter=',')
    #print (csv_data)
    for row in csv_data:
        cursor.bindarraysize = 1
        cursor.setinputsizes(int, 20, float)
        print("iB4 insert")
        print(row)
        cursor.execute('insert into muni4 (srollno, name1, efees) VALUES(:1, :2, :3)', row)
        print("AF insert")

    #cursor.execute("create table newtable45(srollno number, name1 varchar2(10), efees number(10, 2))")
    print("After table create")
    #rows = [(1, 'Bob', 11.22), (2, 'Kim', 27.33)]
    rows = [(5, 'Bob123', 11.22)]
        cursor.bindarraysize = 1
    cursor.setinputsizes(int, 20, float)
    cursor.executemany("insert into muni4(srollno, name1, efees) values (:1, :2, :3)", rows)
    con.commit()
    #stmt2 = "insert into muni4 (srollno,name1,efees) VALUES(\'2345\',\'Muni1234\',\'1234.23\'))"
    #cursor.execute(stmt2)
    stmt = 'select * from muni4'
    cursor.execute(stmt)
    res=cursor.fetchall()
    print(res)
    #cursor.execute('insert into muni4 (srollno,name1, efees) VALUES ('1234','Third123', '1012.12');')              
    #cursor.execute("describe  muni4")
    print("Table Created successful")

except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)

# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()

