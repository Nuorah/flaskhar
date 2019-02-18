from flask import Blueprint

conway = Blueprint(
    'conway',
    __name__,
    template_folder='../templates',
    static_folder="../static",
)

from . import routes