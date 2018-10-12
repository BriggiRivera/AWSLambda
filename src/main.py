import sys
import boto3
from S3.S3Manager import S3Manager

def main(argv):
    manager = S3Manager("briggi-rivera-guillen-pictures")
    manager.upload("D:\\Juan\\Celular\\20181010\\Nuclear.jpg", "nuclear.jpg")

if __name__ == "__main__":
    main(sys.argv)