#Emerging Tech Project: Antaine Ó Conghaile - G00347577

from flask import Flask,render_template,request
import flask as fl
import numpy as np
import keras as kr 
import tensorflow as tf
import base64
import cv2
from PIL import Image, ImageOps
#from keras.models import load_mode
#from tensorflow import keras
#from tensorflow.keras import layers
#from tensorflow.keras.models import Sequential, load_model
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.models import Sequential
#from keras.models import load_model


#with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
 #   file_content = f.read()
#Test login credentials
app = fl.Flask(__name__)
model = kr.models.load_model('model.h5')

#Variables
x = 28
y = 28
area = y, x

#graph = tf.get_default_graph()


#model =  kr.models.load_model('model.h5')
#model = kr.models.load_model('model.h5')

@app.route('/')
def home():
	return app.send_static_file('canvas.html')


@app.route('/image',methods=['POST'])
def getImage():

	global graph
	with graph.as_default():
		cryptImage = fl.request.values[('imgBase64')]
		deImage = base64.b64decode(cryptImage[22:])

		with open ('image.png', 'wb') as f:
			f.write(deImage)
		userImage = Image.open("image.png")

	   	# Resizing the image so it is suitable for the MNIST dataset
	   	# Sourced from: https://github.com/python-pillow/Pillow/blob/3.0.x/docs/reference/Image.rst
		mnistImage = ImageOps.fit(userImage, area, Image.ANTIALIAS)

	    # Saving and loading the new resized images
		mnistImage.save("newImage.png")
		newImage = cv2.imread("newImage.png")

	    # Soruced from: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python
	    # Reshaping and adding to nparray
		grayScaleImage = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
	    # Converting to float32 and dividing by 255 for attempted normilization(Does not really impact accuracy of web app)
		grayScaleArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
		grayScaleArray /= 255

		return null

app.run()

#@app.route('/predict', methods=['GET','POST'])
#def calculate():
		#howmany = int(fl.request.values.get("noofnos", "1"))
#		return null

#print("hello")
