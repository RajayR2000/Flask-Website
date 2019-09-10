from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddOwner(FlaskForm):
    id=IntegerField("Enter the id for the puppy:")
    name=StringField("Enter your name:")
    submit=SubmitField()
