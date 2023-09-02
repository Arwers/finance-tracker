from flask import Flask, render_template


# Check in future, __name__ param can be buggy
app = Flask(__name__, template_folder="templates")


# list of dictionaries of expenses
expenses = [
    {"name": "expense1", "cost": 300, "date": "11.11.2023"},
    {"name": "expense2", "cost": 150, "date": "02.11.2020"},
    {"name": "expense3", "cost": 50, "date": "14.11.203"},
]


@app.route("/")
def index():
    return render_template("index.html", expenses=expenses)


if __name__ == "__main__":
    app.run(debug=True)
