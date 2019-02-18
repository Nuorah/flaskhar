from flask import Flask
from .home import home
from .pow import pow
from .conway import conway
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(pow, url_prefix='/pow')
app.register_blueprint(conway, url_prefix='/conway')