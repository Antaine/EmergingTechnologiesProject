#Emerging Tech Project: Antaine Ó Conghaile - G00347577

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

print("String(hello()")