from flask import Blueprint, render_template

second = Blueprint("second", __name__, static_folder="static", template_folder="templates") # second come nome del file

@second.route("/home")
@second.route("/")
def second_home():
    return render_template("home.html")