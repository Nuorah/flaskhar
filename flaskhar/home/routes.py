from . import home
from flask import render_template

@home.route('/')
@home.route('/index')
def index():
    return render_template("index.html")

@home.route('/python')
def python():
    return render_template("python.html")