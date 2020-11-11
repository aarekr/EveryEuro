from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BudgetForm(FlaskForm):
    month = StringField("Jan")
    salary = IntegerField("Salary", validators=[validators.NumberRange(min=500, max=10000)])
    mortgagerent = IntegerField("Mortgage/rent", validators=[validators.NumberRange(min=100, max=2000)])
    balance = IntegerField("Balance")

    class Meta:
        csrf = False
