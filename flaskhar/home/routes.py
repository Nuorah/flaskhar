from . import home
from flask import render_template

@home.route('/')
@home.route('/index')
def index():
    return render_template("index.html")

@home.route('/projets')
def projets():
    return render_template("projets.html")