from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/env')
def hello_world():
    return 'DISCLOSED_STRING'

@app.route('/secret-env')
def hello_world():
    return 'SECRET_STRING'