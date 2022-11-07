from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired

CHOICES_YN = [(False, ""), ("1", "Yes"), ("0", "No")]


class AddCafe(FlaskForm):
    name = StringField(label="Cafe Name", validators=[InputRequired()])
    map_url = StringField(label="Map URL", validators=[InputRequired()])
    img_url = StringField(label="Image URL", validators=[InputRequired()])
    location = StringField(label="Location", validators=[InputRequired()])
    has_sockets = SelectField(label="Socket Availability",
                              choices=CHOICES_YN,
                              validators=[InputRequired()])
    has_toilet = SelectField(label="Restroom Availability",
                             choices=CHOICES_YN,
                             validators=[InputRequired()])
    has_wifi = SelectField(label="Wifi Availability",
                           choices=CHOICES_YN,
                           validators=[InputRequired()])
    can_take_calls = SelectField(label="Able to Make/Take Calls",
                                 choices=CHOICES_YN,
                                 validators=[InputRequired()])
    seats = SelectField(label="Number of Seats",
                        choices=["", "0-10", "10-20", "20-30", "30-40", "50+"],
                        validators=[InputRequired()])
    coffee_price = StringField(label="Coffee Price (e.g. $4.00)", validators=[InputRequired()])
    submit = SubmitField(label="Submit")
    cancel = SubmitField(label="Cancel")
