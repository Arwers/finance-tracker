from flask import Blueprint, render_template, request, redirect, url_for
from .utils import *


homepage = Blueprint(
    "homepage", __name__, template_folder="templates", static_folder="static"
)

categories = [
    "food",
    "car",
    "house",
    "health",
    "taxes",
    "other",
]

expenses = [
    {"name": "expense1", "cost": 300, "date": "11.11.2023", "category": "food"},
    {"name": "expense2", "cost": 150, "date": "02.11.2020", "category": "car"},
    {"name": "expense3", "cost": 50, "date": "14.11.203", "category": "food"},
]

total_cost = total_cost_count(expenses)
category_cost = {key: 0 for key in ["total"] + categories}
print(category_cost)
limit = 2000


@homepage.route("/")
def index():
    return render_template(
        "index.html",
        expenses=expenses,
        total_cost=total_cost,
        limit=limit,
        categories=categories,
    )


@homepage.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    cost = int(request.form["cost"])
    date = request.form["date"]
    category = request.form["category"]

    expenses.append({"name": name, "cost": cost, "date": date, "category": category})
    global total_cost
    total_cost += cost

    return redirect(url_for("homepage.index"))


@homepage.route("/add_limit", methods=["POST"])
def add_limit():
    global limit
    limit = request.form["limit"]

    return redirect(url_for("homepage.index"))


@homepage.route("/delete/<int:index>")
def delete(index):
    cost = expenses[index]["cost"]
    global total_cost
    total_cost -= cost

    del expenses[index]
    return redirect(url_for("homepage.index"))
