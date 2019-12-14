#Emerging Tech Project: Antaine Ó Conghaile - G00347577

#Imports
from flask import Flask,render_template,request
import flask as fl
import numpy as np
import keras as kr 
import tensorflow as tf
import tensorflow.keras
import base64
import cv2
from PIL import Image, ImageOps

#Variables
app = fl.Flask(__name__)
model = kr.models.load_model('model.h5')
model._make_predict_function() 
#Resizing
x = 28
y = 28
area = y, x

#Home
@app.route('/')
def home():
	return app.send_static_file('canvas.html')


#Connects html to python
@app.route('/image',methods=['POST'])
def getImage():
	#Get Image Data
	cryptImage = fl.request.values[('imgBase64')]
	#Decrypt
	deImage = base64.b64decode(cryptImage[22:])
	#Open Image & Save
	with open ('image.png', 'wb') as f:
		f.write(deImage)
	userImage = Image.open("image.png")
	#Resized
	resizeImage = ImageOps.fit(userImage, area, Image.ANTIALIAS)

	# Saving and loading the new resized images
	resizeImage.save("resize.png")
	newImage = cv2.imread("resize.png")

	# Convert to Grayscale
	grayScaleImage = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
		    # Converting to float32 and dividing by 255 for attempted normilization(Does not really impact accuracy of web app)
	grayScaleArray = np.array(grayScaleImage, dtype=np.float32).reshape(1, 784)
	grayScaleArray /= 255

	#Set & Get Calculation
	setCalculation = model.predict(grayScaleArray)
	getCalculation = np.array(setCalculation[0])

	#Predection
	result = str(np.argmax(getCalculation))
	print(result)

	#Return Number Predectioon
	return result

#Run  App
if __name__ == "__main__":
    app.run
