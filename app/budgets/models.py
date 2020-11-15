from app import db
from sqlalchemy.sql import text

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    month = db.Column(db.String(144), nullable=False)
    name = db.Column(db.String(144), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    mortgagerent = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, month, name, salary, mortgagerent, balance):
        self.month = month
        self.name = name
        self.salary = salary
        self.mortgagerent = mortgagerent
        self.balance = balance


    @staticmethod
    def month_name_info(): # checking if month is already entered
        stmt = text("SELECT name FROM Budget")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"name":row[0]})
        return response
