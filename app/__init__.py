from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///budgets.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

from app import routes

db.create_all()
