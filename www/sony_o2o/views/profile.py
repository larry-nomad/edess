from flask import Blueprint
from flask import render_template

BP = Blueprint('profile', __name__)


@BP.route('profile')
def profile():
    return render_template("profile.html")
