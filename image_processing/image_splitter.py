import os
import sys
import cv2
import numpy as np

pig_directory = "isolated_pig_images"
weight_directory = "isolated_weight_images"
animal_nr_directory = "isolated_animal_nr_images"
run_nr_directory = "isolated_run_nr_images"


def directories_check():
    if not os.path.exists(pig_directory):
        os.makedirs(pig_directory)

    if not os.path.exists(weight_directory):
        os.makedirs(weight_directory)

    if not os.path.exists(animal_nr_directory):
        os.makedirs(animal_nr_directory)

    if not os.path.exists(run_nr_directory):
        os.makedirs(run_nr_directory)


def splitter(directory):
    # directories
    pig_directory = "isolated_pig_images"
    weight_directory = "isolated_weight_images"
    animal_nr_directory = "isolated_animal_nr_images"
    run_nr_directory = "isolated_run_nr_images"

    # iterate over files
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(file):
            print(os.path.splitext(filename)[0])

            # image resizing just in case images are not in the right sizes
            im = cv2.imread(file)
            im = cv2.resize(im, (512, 512))
            imgheight, imgwidth, channels = im.shape

            # separate the image into 3 vertical parts and then rejoin two of them to get the animals image
            vertical_cuts(imgheight, imgwidth, im, filename, pig_directory)
            # read the first third of the image to process it into the 3 respective folders
            im = cv2.imread(os.path.splitext(filename)[0]+"1.jpg")
            horizontal_cuts(imgheight, imgwidth, im, filename, weight_directory, animal_nr_directory, run_nr_directory)
            # deletion of the images that are of no use from the folder
            clean_residual_images(filename)


def vertical_cuts(imgheight, imgwidth, im, filename, pig_directory):
    rows = imgheight // 1
    columns = imgwidth // 3

    filename_extension = 0
    for y in range(0, imgheight, rows):
        for x in range(0, imgwidth, columns):
            filename_extension += 1
            tiles = im[y:y + rows, x:x + columns]
            cv2.imwrite(os.path.splitext(filename)[0] + str(filename_extension) + ".jpg", tiles)

    img1 = cv2.imread(os.path.splitext(filename)[0] + "2.jpg")
    img2 = cv2.imread(os.path.splitext(filename)[0] + "3.jpg")
    vis = np.concatenate((img1, img2), axis=1)
    cv2.imwrite(os.path.join(pig_directory, os.path.splitext(filename)[0] + "_pig.jpg"), vis)


def horizontal_cuts(imgheight, imgwidth, im, filename, weight_directory, animal_nr_directory, run_nr_directory):
    rows = imgheight // 3
    columns = imgwidth // 1

    filename_extension = 0
    for y in range(0, imgheight, rows):
        for x in range(0, imgwidth, columns):
            filename_extension += 1
            tiles = im[y:y + rows, x:x + columns]
            if filename_extension == 1:
                cv2.imwrite(os.path.join(animal_nr_directory, os.path.splitext(filename)[0] + "_animal_nr.jpg"),
                            tiles)
            if filename_extension == 2:
                cv2.imwrite(os.path.join(weight_directory, os.path.splitext(filename)[0] + "_weight.jpg"), tiles)
            if filename_extension == 3:
                cv2.imwrite(os.path.join(run_nr_directory, os.path.splitext(filename)[0] + "_run_nr.jpg"), tiles)


def clean_residual_images(filename):
    # clean the useless split base images
    for i in range(1, 5):
        if os.path.isfile(os.path.splitext(filename)[0] + str(i) + ".jpg"):
            os.remove(os.path.splitext(filename)[0] + str(i) + ".jpg")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error, this application needs 1 parameters to run!")
        print("Usage: python3 image_splitter.py folder_with_images_to_process ()")
        sys.exit()

    if len(sys.argv[1]) > 0:
        directory_name = sys.argv[1]
        directories_check()
        splitter(directory_name)
