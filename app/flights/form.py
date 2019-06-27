from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField
from wtforms.fields.html5 import  DateField, DateTimeLocalField
from wtforms.validators import DataRequired

class FlightForm(FlaskForm):
    departure = DateTimeLocalField('Departure date', format='%Y-%m-%dT%H:%M')
    arrival = DateTimeLocalField('Arrival date', format='%Y-%m-%dT%H:%M')
    seats = IntegerField('Number of seats', validators=[DataRequired()])
    price = DecimalField('Ticket price', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TouristForm(FlaskForm):
    fstname = StringField('First name', validators=[DataRequired()])
    lstname = StringField('Last name', validators=[DataRequired()])
    gender = StringField('Gender', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    remarks = StringField('Remarks')
    birth = DateField('Date of birth', validators=[DataRequired()])
    submit = SubmitField('Submit')
