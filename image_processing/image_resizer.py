import os
import sys
import cv2


def resizer(input_dir, output_dir):
    # iterate over files
    for filename in os.listdir(input_dir):
        file = os.path.join(input_dir, filename)
        # checking if it is a file
        if os.path.isfile(file):
            print(os.path.splitext(filename)[0])

            im = cv2.imread(file)
            im = cv2.resize(im, (512, 512))

            cv2.imwrite(os.path.join(output_dir, os.path.splitext(filename)[0] + '.jpg'), im)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error, this application needs 2 parameters to run!")
        print("Usage: python3 image_resizer.py input_folder_with_images output_folder_to_save_resized_images")
        sys.exit()

    if len(sys.argv[1]) > 0:
        INPUT_DIRECTORY = sys.argv[1]
        OUTPUT_DIRECTORY = sys.argv[2]
        resizer(INPUT_DIRECTORY, OUTPUT_DIRECTORY)

