from flask import Blueprint
from flask import render_template

BP = Blueprint('index', __name__)


@BP.route('/')
def frontend():
	    return render_template("index.html")
