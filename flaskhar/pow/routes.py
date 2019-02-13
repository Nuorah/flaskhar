from flask import render_template
from . import pow
from .forms import PowForm

@pow.route('/', methods=['GET', 'POST'])
def pow():
    form = PowForm()
    return render_template("pow.html", form=form)
