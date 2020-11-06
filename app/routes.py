from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")  # remove this?
def app_page():
    return render_template("app/app_page.html")

@app.route("/app/overview")
def overview():
    return render_template("app/overview.html")

@app.route("/app/jan")
def jan():
    return render_template("app/jan.html")
