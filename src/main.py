import sys
import boto3
import os

from os import listdir
from os.path import isfile, join
from S3.S3Manager import S3Manager

def main(argv):

    directory = argv[1]
    print(directory)
    pictures = [picture for picture in listdir(directory) if isfile(join(directory, picture)) and picture.endswith('.jpg')]
    manager_input = S3Manager("briggi-rivera-guillen-pictures")
    manager_output = S3Manager("briggi-rivera-guillen-pictures-transformed")
    
    for picture in pictures:
        manager_input.upload(directory, picture)
    
    output_directory = join(directory, "Procesados")
        
    for picture in pictures:
        print(picture)
        manager_output.download(output_directory, picture)

if __name__ == "__main__":
    main(sys.argv)