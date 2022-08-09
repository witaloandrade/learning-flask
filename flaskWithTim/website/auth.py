from xmlrpc.client import boolean
from flask import Blueprint , render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    # return "<p>Login</p>"
    return render_template("login.html",boolean=False)


@auth.route('/logout')
def logout():
    return "<p>LogOut</p>"
    

@auth.route('/sign-up')
def sign_up():
    # return "<p>Sign Up</p>"
    return render_template("signup.html")