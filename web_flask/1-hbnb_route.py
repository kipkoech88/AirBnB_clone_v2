#!/usr/bin/python3
"""
Initialize Flask app
with two routes
with strict_slashes=False
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays HBNB
    when user navigates to the URL
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
