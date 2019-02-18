from flask import render_template
from . import conway


@conway.route('/', methods=['GET', 'POST'])
def conway():
    pass