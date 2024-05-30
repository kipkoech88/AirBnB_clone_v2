#!/usr/bin/python3
"""
This is a script that will
start the web application
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")