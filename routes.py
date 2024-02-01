from flask import Blueprint
from controller import grade

helloword = Blueprint("helloworld",__name__)

@helloword.route("/")
def welcome():
    return "Hello world"

@helloword.route("/scoreCheck")
def scorecheck():
    return grade(0)