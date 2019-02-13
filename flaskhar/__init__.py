from flask import Flask
from .home import home
from .pow import pow
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(pow, url_prefix='/pow')