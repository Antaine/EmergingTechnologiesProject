#Emerging Tech Project: Antaine Ó Conghaile - G00347577

from flask import Flask, escape, request
import numpy as np
import pandas as pd
import gzip

#with gzip.open('data/t10k-images-idx3-ubyte.gz', 'rb') as f:
 #   file_content = f.read()

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

print("String(hello()")