from flask import Blueprint
from flask import render_template

BP = Blueprint('hot', __name__)


@BP.route('hot')
def hot():
    return render_template("hot.html")
