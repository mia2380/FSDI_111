from flask import Flask  # from the flask module, import the Flask class
from flask import render_template

from datetime import datetime


# create an instance of the Flask class into app (now an object)
app = Flask(__name__)
# Class is to object as blueprint is to house.


@app.get("/")  # A decorator that allows us to map a route to a "view function"
def index():  # Flask calls fuctions mapped to routes "view functions"
    out = {  # Flask will automatically convert dictionaries to JSON for convenience
        "first_name": "Brenda",
        "last_name": "Allemand",
        "hobbies": "Photography",
        "isActive": True
    }
    return out  # if we wish to build a RESTful service, this is a good convension to follow
    # as JSON is the most common data format for RESTful services


@app.get("/about")
def about():
    time_stamp = datetime.now().strftime("%F %H:%M:%S")
    return render_template("about.html", timestamp=time_stamp)
