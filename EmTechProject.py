#Emerging Tech Project: Antaine Ó Conghaile - G00347577

from flask import Flask, escape, request
import flask as fl
import numpy as np
import keras as kr 
import tensorflow as tf
import base64
import cv2
from PIL import Image, ImageOps
#graph = tf.get_default_graph()
#with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
 #   file_content = f.read()
#Test login credentials
app = fl.Flask(__name__)

#Variables
x = 28
y = 28
area = y, x


@app.route('/')
def home():
	return app.send_static_file('canvas.html')


@app.route('/image',methods=['POST'])
def getImage():
	cryptImage = fl.request.values[('imgBase64')]
	deImage = base64.b64decode(cryptImage[22:])

	with open ('image.png', 'wb') as f:
		f.write(deImage)
		numImage = Image.open(image.png)
	

	# Resize img
	mnistImage = ImageOps.fit(numImage, size, Image.ANTIALIAS)
	#Save Image	
	mnistImage.save("reImg.png")
	numImage = cv2.imread("reImg.png")

	gSImg = cv2.cvtColor(reImg, cv2.COLOR_BGR2GRAY)
	gSArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
	grayScaleArray /= 255

	return null

app.run()

#@app.route('/predict', methods=['GET','POST'])
#def calculate():
		#howmany = int(fl.request.values.get("noofnos", "1"))
#		return null

#print("hello")
