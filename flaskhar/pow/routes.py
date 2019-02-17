from flask import render_template
from . import pow
from .proofofwork import find_nonce
from .forms import PowForm

@pow.route('/', methods=['GET', 'POST'])
def pow():
    form = PowForm()
    if form.validate_on_submit():
        nonce, hash_result = find_nonce(form.block.data, form.difficulty.data)
        return render_template("pow.html", form=form, nonce=nonce, hash_result=hash_result)
    return render_template("pow.html", form=form)
