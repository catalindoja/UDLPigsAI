import sys
import os
import cv2
from skimage.metrics import structural_similarity
import argparse
import imutils
import filecmp

# cv2 SSIM
# Usage:
# python3 image_difference.py -f ./output/capture0020.png -s ./output/capture0137.png



def image_comparator(folder):

    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(file):
            for filename2 in os.listdir(directory):
                file2 = os.path.join(directory, filename2)
                # checking if it is a file
                if os.path.isfile(file):
                    if filecmp.cmp(file, file2):
                        pass
                    else:
                        print(file)
                        #Load the two input images
                        image_a = cv2.imread(file)
                        image_b = cv2.imread(file2)

                        # Convert the images to grayscale
                        gray_a = cv2.cvtColor(image_a, cv2.COLOR_BGR2GRAY)
                        gray_b = cv2.cvtColor(image_b, cv2.COLOR_BGR2GRAY)

                        # Compute the Structural Similarity Index (SSIM) between the two
                        # images, ensuring that the difference image is returned
                        (score, diff) = structural_similarity(gray_a, gray_b, full=True)
                        diff = (diff * 255).astype("uint8")

                        # You can print only the score if you want
                        print("SSIM: {}".format(score))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error, this application needs 1 parameters to run!")
        sys.exit()

    if len(sys.argv[1]) > 0:
        directory = sys.argv[1]
        image_comparator(directory)
