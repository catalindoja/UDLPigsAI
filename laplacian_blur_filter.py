import cv2
import os


def calculate_focal_measure(img):
    # convert RGB image to Gray scale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Measure focal measure score (laplacian approach)
    fm = cv2.Laplacian(gray, cv2.CV_64F).var()
    return fm




# assign directory
directory = 'output/'

# iterate over files in
# that directory
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(file):
        print(file)
        image = cv2.imread(file)
        focal_measure = calculate_focal_measure(image)
        print("focal-measure-score", focal_measure)

        if focal_measure > 100:
            status = "Non Blurry"
            print("non blurry")
            color = (255, 0, 0)
        else:
            status = "Blurry"
            print("blurry")
            color = (0, 0, 255)
            os.remove(file)
