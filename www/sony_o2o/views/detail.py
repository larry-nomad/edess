from flask import Blueprint
from flask import render_template

BP = Blueprint('detail', __name__)


@BP.route('detail/<int:id>')
def detail(id):
    return render_template("detail.html")
