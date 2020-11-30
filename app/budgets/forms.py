from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators
from app.budgets.models import Budget

class BudgetForm(FlaskForm):
    month = StringField("Month")
    name = StringField("Month")
    salary = IntegerField("Salary", [validators.DataRequired(), validators.NumberRange(min=500, max=10000)])
    mortgagerent = IntegerField("Mortgage/rent", [validators.DataRequired(), validators.NumberRange(min=100, max=2000)])
    left_to_budget = IntegerField("Left to budget")

    def validate_month(self, name):
        month = Budget.query.filter_by(name=name.data).first()
        if month is not None: # month already entered
            raise validationError("Month already entered")

    class Meta:
        csrf = False

