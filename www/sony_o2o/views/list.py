from flask import Blueprint
from flask import render_template

BP = Blueprint('list', __name__)


@BP.route('list/<string:type>')
def list(type):
    return render_template("list.html", page = type)
