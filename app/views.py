"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
import os
import time
from app import app
from flask import render_template, request, redirect, url_for
from app import db
from app.models import Users
from .forms import UserProfile
from flask import jsonify
import models
from app.models import ProfileSchema
from werkzeug import secure_filename
from flask_wtf.file import FileField

###
# Routing for your application.
###

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/persons')
def person():
  first_user = db.session.query(Users).first()
  return jsonify()

@app.route("/profile/" , methods=["GET" , "POST"])
def profile():
  form = UserProfile()
  if request.method == 'POST':
    file = request.files['image']
    image = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], image))
    firstname = form.firstname.data
    lastname = form.lastname.data
    age = form.age.data
    sex = form.sex.data
    goingtoadd=Users(image, firstname, lastname, age, sex)
    db.session.add(goingtoadd)
    db.session.commit()
    return render_template('profile.html', form=form)
  return render_template('profile.html', form=form)

@app.route("/profiles/", methods=["GET" , "POST"])
def profiles():
  users=models.Users.query.all()
  if request.method=="POST":
    myData=ProfileSchema(many=True)
    data= myData.dump(user)
    return jsonify({"Users": data.data})
  return render_template('userprofile.html', users=users)
  

@app.route("/profile/<userid>" , methods=["GET" , "POST"])
def profileuserid(userid):
  user = Users.query.filter_by(userid=userid).first()
  if request.method=="POST":
    date=str(user.profile_add_on)
    return jsonify(userid=user.userid, profile_add_on=date, firstname=user.firstname, lastname=user.lastname, age=user.age, sex=user.sex)
  return render_template('user.html', user=user)

  
  
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def timeinfo():
  now = time.strftime("%Y-%m-%d")
  return now

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=8888)
