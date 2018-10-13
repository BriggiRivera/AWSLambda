import sys
import boto3
from S3.S3Manager import S3Manager
from skimage import filters
from scipy import misc

def main(argv):
    manager = S3Manager("briggi-rivera-guillen-pictures")
    #manager.upload("D:\\Juan\\Celular\\20181010\\Esposos.jpg", "JYB.jpg")

    image = misc.imread("D:\\Juan\\Celular\\20181010\\Esposos.jpg", flatten=True)
    edges = filters.sobel(image)
    processed_path = "D:\\Juan\\Celular\\20181010\\Esposos_borders.jpg"
    misc.imsave(processed_path, edges)

if __name__ == "__main__":
    main(sys.argv)