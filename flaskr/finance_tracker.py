from flask import Flask, render_template, request, redirect, url_for


# Check in future, __name__ param can be buggy
app = Flask(__name__, template_folder="templates")


# list of dictionaries of expenses
expenses = [
    {"name": "expense1", "cost": 300, "date": "11.11.2023"},
    {"name": "expense2", "cost": 150, "date": "02.11.2020"},
    {"name": "expense3", "cost": 50, "date": "14.11.203"},
]
# total cost of all expenses
total_cost = 0
for item in expenses:
    total_cost += item["cost"]


@app.route("/")
def index():
    return render_template("index.html", expenses=expenses, total_cost=total_cost)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    cost = int(request.form["cost"])
    date = request.form["date"]
    expenses.append({"name": name, "cost": cost, "date": date})
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del expenses[index]
    return redirect(url_for("index"))


@app.get("/update")
def update():
    global gen_total  # get the global iterator

    # return the next value in iterator
    return str(next(gen_total))


if __name__ == "__main__":
    app.run(debug=True)
