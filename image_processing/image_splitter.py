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

            im = cv2.imread(file)
            im = cv2.resize(im, (512, 512))
            # cv2.imwrite(os.path.join("./", os.path.splitext(filename)[0] + "_2.jpg"), im)
            imgheight, imgwidth, channels = im.shape

            # M is the number of rows, N is the number of columns
            m = imgheight//1
            n = imgwidth//3

            val1 = 0
            for y in range(0, imgheight, m):
                for x in range(0, imgwidth, n):
                    val1 += 1

                    tiles = im[y:y+m, x:x+n]

                    cv2.imwrite(os.path.splitext(filename)[0] + str(val1)+".jpg", tiles)

            img1 = cv2.imread(os.path.splitext(filename)[0]+"2.jpg")
            img2 = cv2.imread(os.path.splitext(filename)[0]+"3.jpg")
            vis = np.concatenate((img1, img2), axis=1)
            cv2.imwrite(os.path.join(pig_directory, os.path.splitext(filename)[0]+"_pig.jpg"), vis)

            # read the first third of the image to process it into the 3 respective folders
            im = cv2.imread(os.path.splitext(filename)[0]+"1.jpg")
            # M is the number of rows, N is the number of columns
            m = imgheight//3
            n = imgwidth//1

            val1 = 0
            for y in range(0, imgheight, m):
                for x in range(0, imgwidth, n):
                    val1 += 1
                    tiles = im[y:y+m, x:x+n]
                    if val1 == 1:
                        cv2.imwrite(os.path.join(animal_nr_directory, os.path.splitext(filename)[0]+"_animal_nr.jpg"),
                                    tiles)
                    if val1 == 2:
                        cv2.imwrite(os.path.join(weight_directory, os.path.splitext(filename)[0]+"_weight.jpg"), tiles)
                    if val1 == 3:
                        cv2.imwrite(os.path.join(run_nr_directory, os.path.splitext(filename)[0]+"_run_nr.jpg"), tiles)

            # clean the useless splitted base images
            for i in range(1, 5):
                if os.path.isfile(os.path.splitext(filename)[0] + str(i)+".jpg"):
                    os.remove(os.path.splitext(filename)[0] + str(i)+".jpg")



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Error, this application needs 1 parameters to run!")
        print("Usage: python3 image_splitter.py folder_with_images_to_process ()")
        sys.exit()

    if len(sys.argv[1]) > 0:
        directory_name = sys.argv[1]
        directories_check()
        splitter(directory_name)
