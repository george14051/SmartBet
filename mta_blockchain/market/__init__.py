from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///betYouSmart.db'
app.config['SQLALCHEMY_ECHO'] = True  # sending SQL-logs to stderr
app.config['SECRET_KEY'] = '2951c323a8753db56414d2b2'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
from market import models