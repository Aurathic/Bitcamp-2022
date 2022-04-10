from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import *

class UserPrefForm(FlaskForm):
    low_price = IntegerField('Low Price')
    high_price = IntegerField('High Price', validators=[NumberRange(0,6000)])
    performance = IntegerField('Performance', widget=RangeInput())
    portability = IntegerField('Portability', widget=RangeInput())