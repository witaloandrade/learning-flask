from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    #return "<h1> Hello Home</h1>"
    return render_template("home.html")