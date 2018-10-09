from flask import Flask, request, redirect, url_for, render_template
from . import app, auth


@app.route("/", methods = ['POST'])
@auth.auth_required
def index():
    pass



@app.route("/signin/user", methods = ['POST'])
def signin_user():
    return render_template('signup.html')

@app.route("/signup/user", methods = ['POST'])
def signup_user():
    return render_template('signup.html')

@app.route("/signin")
def sign_in():
    #verify password 
    return render_template("signin.html")

@app.route("/signup")
def sign_up():
    #add username and password to database
    return redirect(url_for("signin")) 

@app.route("/error")
def error(error_value=None):
    return render_template("error.html", error_value = error_value)