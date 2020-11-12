from flask import render_template, request, redirect, url_for
from app import app, db
from app.budgets.models import Budget
from app.budgets.forms import BudgetForm

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
    form = BudgetForm(request.form)
    return render_template("app/jan.html", all_months = Budget.query.all(), form=form)

@app.route("/app/jan/create", methods=["POST"])
def create_jan():
#    salary = int(request.form.get("salary"))
#    rent = -int(request.form.get("rent"))
#    balance = salary+rent
    form = BudgetForm(request.form)
    if not form.validate():
        return render_template("app/jan.html", all_months = Budget.query.all(), form=form)

    jan = Budget(form.month.data, form.salary.data, form.mortgagerent.data, (form.salary.data-form.mortgagerent.data))
#    print("***** jan: ", jan)
    jan.salary = form.salary.data
    jan.mortgagerent = form.mortgagerent.data
    jan.balance = (jan.salary - jan.mortgagerent)

    print("*****Salary : ", jan.salary)
    print("*****Rent   : ", jan.mortgagerent)
    print("*****Balance: ", jan.balance)

    db.session().add(jan)
    db.session().commit()

    return redirect(url_for("jan"))
