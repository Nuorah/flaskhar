from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, NumberRange

class PowForm(FlaskForm):
    block = StringField('Block', [validators.DataRequired("Texte requis")])
    difficulty = IntegerField('Password', [validators.NumberRange(1, 16, "Entrez un entier entre 1 et 16"),
                                           validators.DataRequired("Entier requis")])
    submit = SubmitField('Mine')