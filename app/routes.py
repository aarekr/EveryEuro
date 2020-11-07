from flask import render_template, request
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

@app.route("/app/jan/create", methods=["POST"])
def create_jan():
    salary = request.form.get("salary")
    rent = request.form.get("rent")
    balance = int(salary)-int(rent)
    print("*****Salary : ", request.form.get("salary"))
    print("*****Rent   : ", request.form.get("rent"))
    print("*****Balance: ", balance)
    return render_template("app/jan.html")
