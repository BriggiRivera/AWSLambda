import boto3

class S3Manager:
    def __init__(self, bucketName):
        self.s3Client = boto3.client('s3')
        self.bucket_name = bucketName
        
    def upload(self, fullPath, name):
        self.s3Client.upload_file(fullPath, self.bucket_name, name)
