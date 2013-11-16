from flask import Blueprint
from flask import render_template

BP = Blueprint('search', __name__)


@BP.route('search')
def search():
    return render_template("search.html")
