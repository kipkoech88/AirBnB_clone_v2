#!/usr/bin/python3
"""
Initialize Flask app
with two routes
with strict_slashes=False
"""
from flask import Flask, render_template


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


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """ Takes in a text
    variable and displays
    c variabe """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pycool(text="is cool"):
    """ Display Python
    + passed in arg or
    default text"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def is_a_number(n):
    """ Displays  is a number
    else returns an error """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def temp(n):
    """ Passes n
    and renders it
    in the template
    """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
