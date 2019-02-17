from flask import Blueprint

pow = Blueprint(
    'pow',
    __name__,
    template_folder='../templates',
    static_folder="../static",
)

from . import routes