from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BudgetForm(FlaskForm):
    month = StringField("Month")
    salary = IntegerField("Salary", [validators.Length(min=3)])
    mortgagerent = IntegerField("Mortgage/rent")
    balance = IntegerField("Balance")

    class Meta:
        csrf = False
