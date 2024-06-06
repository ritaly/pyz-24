from database import db


class Expense(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    description = db.Column(db.String(200), unique=False, nullable=False)
    amount = db.Column(db.Float, unique=False, nullable=False)
    date = db.Column(db.Date, nullable=True)