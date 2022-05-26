import cv2
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

image = cv2.imread('test0.jpg') #--imread() helps in loading an image into jupyter including its pixel values
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 3x3 array for edge detection
mat_y = np.array([[-1, -2, -1],
                  [0, 0, 0],
                  [1, 2, 1]])
mat_x = np.array([[-1, 0, 1],
                  [0, 0, 0],
                  [1, 2, 1]])

filtered_image = cv2.filter2D(gray, -1, mat_y)
plt.imshow(filtered_image, cmap='gray')
filtered_image = cv2.filter2D(gray, -1, mat_x)
plt.imshow(filtered_image, cmap='gray')

plt.show()
