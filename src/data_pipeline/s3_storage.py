import boto3
import json

def upload_to_s3(data, bucket_name, file_name):
    s3 = boto3.client("s3")
    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data)
    )
    print(f"Data uploaded to {bucket_name}/{file_name}")
