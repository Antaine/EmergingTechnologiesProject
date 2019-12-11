#Emerging Tech Project: Antaine Ó Conghaile - G00347577

from flask import Flask, escape, request
import flask as fl

#with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
 #   file_content = f.read()
#Test login credentials
app = fl.Flask(__name__)

@app.route('/')
def home():
	return app.send_static_file('canvas.html')

#@app.route('/predict', methods=['GET','POST'])
#def calculate():
		#howmany = int(fl.request.values.get("noofnos", "1"))
#		return null

#print("hello")
