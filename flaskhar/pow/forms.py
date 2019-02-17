from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms import validators
from wtforms.validators import DataRequired, NumberRange

class PowForm(FlaskForm):
    block = StringField('Block', [validators.DataRequired("Needs text.")])
    difficulty = IntegerField('Difficulty', [validators.NumberRange(1, 16, "Needs an integer between 1 and 16."),
                                           validators.DataRequired("Needs an integer between 1 and 16.")])
    submit = SubmitField('Mine')