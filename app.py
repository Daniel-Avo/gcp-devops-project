import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/env')
def env():
    return os.environ["DISCLOSED_STRING"]

@app.route('/secret')
def secret():
    return os.environ["SECRET_STRING"]