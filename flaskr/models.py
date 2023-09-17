from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Expenses(db.Model):
    __tablename__ = "Expenses"

    # keys
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id"))
    
    # values
    name = db.Column(db.String(64))
    cost = db.Column(db.Numeric(10, 2))
    date = db.Column(db.Date())
    category = db.Column(db.String(32))
    
    def __init__(self, name, cost, date, category):
        self.name = name
        self.cost = cost
        self.date = date
        self.category = category


class Users(db.Model):
    __tablename__ = "Users"

    # keys
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # values
    username = db.Column(db.String(32))
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.username = username
        self.password = password

