from flask import render_template

def index():
    return render_template("home.html", title="Welcome to AgilePy")