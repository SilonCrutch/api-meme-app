#!/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "My first api project."

app.run(host="0.0.0.0", port=5001)