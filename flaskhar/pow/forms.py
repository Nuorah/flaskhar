from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, NumberRange

class PowForm(FlaskForm):
    block = StringField('Block', [validators.DataRequired("Texte requis")])
    difficulty = IntegerField('Difficulty', [validators.NumberRange(1, 16, "Entier entre 1 et 16 requis"),
                                           validators.DataRequired("Entier entre 1 et 16 requis")])
    submit = SubmitField('Mine')