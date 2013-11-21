from flask import Blueprint
from flask import render_template

BP = Blueprint('store', __name__)


@BP.route('store')
def store():
    return render_template("store.html")
