from . import db


class Expenses(db.Model):
    __tablename__ = "Expenses"

    # keys
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, foreign_key=True)
    
    # values
    name = db.Column(db.String(64))
    cost = db.Column(db.Numeric(10, 2))
    date = db.Column(db.Date())
    category = db.Column(db.String(32))


class Users(db.Model):
    __tablename__ = "Users"

    # keys
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # values
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))