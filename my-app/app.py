from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def hello():
    response = requests.get('http://counter-service:6000/increment')
    count = response.text
    return f'Hello! This page has been viewed {count} times.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)