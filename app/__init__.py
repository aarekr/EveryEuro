from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///budgets.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from app import routes # all routes via this file

from app.budgets import models

db.create_all()
