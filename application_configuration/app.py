import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASS")
host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}/{db_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
