from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class BudgetForm(FlaskForm):
    month = StringField("Month")
    salary = IntegerField("Salary")
    mortgagerent = IntegerField("Mortgage/rent")

    class Meta:
        csrf = False
