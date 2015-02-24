from.import db
from random import randint
import views
from marshmallow import Schema, fields

class Users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image= db.Column(db.String(120))
  firstname= db.Column(db.String(80))
  lastname= db.Column(db.String(80))
  age= db.Column(db.Integer)
  sex= db.Column(db.String(80))
  userid = db.Column(db.Integer)
  profile_add_on= db.Column(db.Date())
  high_score= db.Column(db.Integer)
  tdollars= db.Column(db.Numeric)
    
  def __init__(self, image, firstname, lastname, age, sex):
    self.image = image
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.sex = sex
    self.userid= randint(1000000, 9999999)
    self.profile_add_on = views.timeinfo()

  def __repr__(self):
    return '<User %r>' % self.firstname
  
class ProfileSchema(Schema):
  name= fields.Method("name")
  
  class Meta:
    fields = ('image', 'firstname', 'lastname', 'age', 'sex', 'userid', 'profile_add_on', 'high_score', 'tdollars')
    
    