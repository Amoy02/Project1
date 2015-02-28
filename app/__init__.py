from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = 'app/static/img'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xsmxlybbtsgtcg:cd8NxxCKdZMcCOSvZ8fQj0rRzk@ec2-23-21-231-14.compute-1.amazonaws.com:5432/d7skpjjq7bn1r'
app.config['SECRET_KEY']= "iloveyou"
db = SQLAlchemy(app)

from app import views, models
