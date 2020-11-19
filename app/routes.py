from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from app import app, db
from app.budgets.models import Budget
from app.budgets.forms import BudgetForm
from app.auth.models import User
from app.auth.forms import LoginForm

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
    form = BudgetForm(request.form)
    print("*****Form   : ", form.name)

    all_months = Budget.query.all()
    print("*****All months: ", all_months)
#    print("*****Budget 1 : ", all_months[0].name)
    if(all_months[0].name == "Jan"): # Jan has to be added somehow
        print("***** Jan on jo syötetty")
    else:
        if not form.validate():
            return render_template("app/jan.html", all_months = Budget.query.all(), form=form)

        jan = Budget(form.month.data, form.name.data, form.salary.data, form.mortgagerent.data, (form.salary.data-form.mortgagerent.data))
        jan.month = form.month.data
        jan.name = "Jan"
        jan.salary = form.salary.data
        jan.mortgagerent = form.mortgagerent.data
        jan.balance = (jan.salary - jan.mortgagerent)

        print("*****jan    : ", jan)
        print("*****Month  : ", jan.month)
        print("*****Name   : ", jan.name)
        print("*****Salary : ", jan.salary)
        print("*****Rent   : ", jan.mortgagerent)
        print("*****Balance: ", jan.balance)

        db.session().add(jan)
        db.session().commit()

    return redirect(url_for("jan"))


# login
@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))

# logout
@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
