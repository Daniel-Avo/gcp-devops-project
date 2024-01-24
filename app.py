from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/env')
def env():
    return 'DISCLOSED_STRING'

@app.route('/secret')
def secret():
    return 'SECRET_STRING'