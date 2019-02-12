from flask import Flask
from .home import home
from .pow import pow

app = Flask(__name__)

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(pow, url_prefix='/pow')