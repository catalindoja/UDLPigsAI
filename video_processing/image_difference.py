import sys
import os
import cv2
from skimage.metrics import structural_similarity
import argparse
import imutils
import filecmp


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def image_comparator(directory, threshold):
    if isfloat(threshold):
        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            print(file)
            # checking if it is a file
            if os.path.isfile(file):
                for filename2 in os.listdir(directory):
                    file2 = os.path.join(directory, filename2)
                    # checking if it is a file
                    if os.path.isfile(file):
                        if filecmp.cmp(file, file2):
                            pass
                        else:
                            print(file2)
                            # load the two input images
                            image_a = cv2.imread(file)
                            image_b = cv2.imread(file2)

                            # convert the images to grayscale
                            gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
                            gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

                            # calculate the similarity index between the two images
                            (score, diff) = structural_similarity(gray_a, gray_b, full=True)
                            diff = (diff * 255).astype("uint8")
                            if score > float(threshold):
                                print(score)
                                os.remove(file2)
    else:
        print("Error the threshold value is not a float value. Exiting program...")
        sys.exit()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error, this application needs 2 parameters to run!")
        print("Usage: python3 image_difference.py directory_name float_threshold_value(Values between 0 and 1. "
              "1 means identical images, 0 mean totally different images)")
        sys.exit()

    if len(sys.argv[1]) and len(sys.argv[2]) > 0:
        directory = sys.argv[1]
        threshold = sys.argv[2]
        image_comparator(directory, threshold)
