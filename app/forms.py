from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalRangeField
from wtforms.validators import DataRequired

class RequestForm(FlaskForm):
    amount = DecimalRangeField('Slide left/right to enter amount in sats', validators=[DataRequired()])
    submit = SubmitField('Submit')

class PayForm(FlaskForm):
    invoice = StringField('Enter BOLT11 string', validators=[DataRequired()])
    submit = SubmitField('Submit')
