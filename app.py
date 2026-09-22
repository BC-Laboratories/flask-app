from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is a test of my enhanced app.... I dream of HTML, lol.'
