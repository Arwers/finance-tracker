from . import expenses

class Engine(expenses.Model):
    # Columns
    id = expenses.Column(expenses.Integer, primary_key=True, autoincrement=True)
    name = expenses.Column(expenses.String(128))
    cost = expenses.Column(expenses.Float, default=0)
    date = expenses.Column(expenses.Date, default=0)
    category = expenses.Column(expenses.String(128), default="other")