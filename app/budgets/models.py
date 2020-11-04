from app import db

class Budget(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    month = db.Column(db.String(144), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    mortgagerent = db.Column(db.Integer, nullable=False)

    def __init__(self, month, salary, mortgagerent):
        self.month = month
        self.salary = salary
        self.mortgagerent = mortgagerent
