from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
import keras as ks
#from keras.datasets import mnist

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

#Import MNIST Datasets
mnist = keras.datasets.mnist
#Load Datasets
(train_images, train_labels), (test_images, test_labels) = ks.datasets.mnist.load_data()
#Class names for options
class_names = ['0', '1', '2', '3', '4','5', '6', 'seven', '8', '9']
#Show W
train_images.shape
len(train_labels)
train_labels
len(test_labels)

#Scale these values to a range of 0 to 1
train_images = train_images / 255.0
test_images = test_images / 255.0

#Layers
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

#Compiler
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

              #Train Model
model.fit(train_images, train_labels, epochs=10)

#Test Model Accuracy
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

#Predections
predictions = model.predict(test_images)
predictions[0]

#Predection
np.argmax(predictions[0])

#Save Model
model.save("model.h5")