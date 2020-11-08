from flask import render_template, request, redirect, url_for
from app import app, db
from app.budgets.models import Budget

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/app")  # remove this?
def app_page():
    return render_template("app/app_page.html")

@app.route("/app/overview")
def overview():
    return render_template("app/overview.html", all_months = Budget.query.all())

@app.route("/app/jan")
def jan():
    return render_template("app/jan.html")

@app.route("/app/jan/create", methods=["POST"])
def create_jan():
    salary = int(request.form.get("salary"))
    rent = int(request.form.get("rent"))
    balance = salary-rent
    print("*****Salary : ", salary)
    print("*****Rent   : ", rent)
    print("*****Balance: ", balance)

    month = Budget("Jan", salary, rent)
    db.session().add(month)
    db.session().commit()

    return redirect(url_for("app/jan.html"))
