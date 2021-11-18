from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'test_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CampTableDB.db'

db = SQLAlchemy(app)

from campr_app import routes