# import the needed libraries
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Activation
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from tensorflow import keras

new_model = keras.models.load_model('./model/model.h5')

new_model.summary()
img_width, img_height = 170, 170 #width & height of input image
input_depth = 1 #1: gray image
#validation_data_dir = 'images_folder_label/validation/' #data validation pathcd
validation_data_dir = 'validate/' #data validation pathcd
epochs = 15 #number of training epoch
batch_size = 4 #training batch size

validation_datagen = ImageDataGenerator(rescale=1/255)

validation_generator = validation_datagen.flow_from_directory(
    validation_data_dir,
    color_mode='grayscale',
    target_size=(img_width,img_height),
    batch_size=batch_size,
    class_mode='categorical')


loss, acc = new_model.evaluate(validation_generator, steps=np.floor(validation_generator.n / batch_size))
print("Accuracy: "+str(acc))
print("Loss: "+str(loss))

