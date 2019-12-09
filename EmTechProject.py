#Emerging Tech Project: Antaine Ó Conghaile - G00347577

from flask import Flask, escape, request
import numpy as np
import pandas as pd
import gzip
import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist
import matplotlib.pyplot as plt

#with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
 #   file_content = f.read()
#Test login credentials
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

print("hello")
(x_train, y_train), (x_test, y_test) = mnist.load_data()
class_names = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
len(train_labels)
