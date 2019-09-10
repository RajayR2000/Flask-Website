from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    name=StringField("Name of Puppy:")
    owner=StringField("Name of Owner:")
    submit=SubmitField("Add Puppy")

class DeleteForm(FlaskForm):
    id=IntegerField("ID of puppy to be removed")
    submit=SubmitField("Delete Puppy")
