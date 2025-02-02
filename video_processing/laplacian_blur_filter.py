import sys
import cv2
import os


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calculate_focal_measure(img):
    # convert RGB image to Gray scale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Measure focal measure score (laplacian approach)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    return fm


def laplacian_filer(directory, threshold):
    if isfloat(threshold):
        # iterate over files
        for filename in os.listdir(directory):
            file = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(file):
                print(file)
                image = cv2.imread(file)
                focal_measure = calculate_focal_measure(image)
                print("focal-measure-score", focal_measure)
                # the int number here is a threshold to be determined
                if focal_measure > float(threshold):
                    print("non blurry")
                else:
                    print("blurry")
                    os.remove(file)
    else:
        print("Error the threshold value is not a float value. Exiting program...")
        sys.exit()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error, this application needs 2 parameters to run!")
        print("Usage: python3 laplacian_blur_filter.py directory_name float_threshold_value(for example 77.95)")
        sys.exit()

    if len(sys.argv[1]) and len(sys.argv[2]) > 0:
        directory = sys.argv[1]
        threshold = sys.argv[2]
        laplacian_filer(directory, threshold)
