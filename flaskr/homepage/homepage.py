from flask import render_template, request, redirect, url_for

# list of dictionaries of expenses
expenses = [
    {"name": "expense1", "cost": 300, "date": "11.11.2023"},
    {"name": "expense2", "cost": 150, "date": "02.11.2020"},
    {"name": "expense3", "cost": 50, "date": "14.11.203"},
]

total_cost = 0
for item in expenses:
    total_cost += item["cost"]

def total_cost_update(new_cost):
    global total_cost
    total_cost += new_cost

@app.route("/")
def index():
    return render_template("index.html", expenses=expenses, total_cost=total_cost)


@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    cost = int(request.form["cost"])
    date = request.form["date"]

    expenses.append({"name": name, "cost": cost, "date": date})
    total_cost_update(cost)
    
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    delated_cost = -expenses[index]["cost"]
    total_cost_update(delated_cost)

    del expenses[index]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
