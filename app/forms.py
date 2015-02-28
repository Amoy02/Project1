from flask.ext.wtf import Form
from wtforms.fields import TextField, SelectField, FileField, SubmitField, IntegerField
from wtforms.validators import Required
from wtforms import validators

class UserProfile(Form):
  image =  FileField('Image File')
  firstname = TextField('First Name', validators=[Required("Please enter your first name")])
  lastname = TextField('Last Name', validators=[Required("Please enter your last name")])
  age = IntegerField('Age',validators=[Required("Please enter your age")])
  sex = SelectField('Sex', choices=[('Female','Female'), ('Male', 'Male')])
  submit = SubmitField("Submit")

  