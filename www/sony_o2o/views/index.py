from flask import Blueprint, session
from flask import render_template

BP = Blueprint('index', __name__)


@BP.route('/')
def index():
    guest = {}
    guest["id"] = session["guest_id"]
    guest["name"] = session["guest_name"]
    return render_template("index.html", guest=guest)
