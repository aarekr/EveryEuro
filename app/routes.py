from flask import render_template
from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")
def app_page():
    print("***** FRONT PAGE")
    return render_template("app/app_page.html")
