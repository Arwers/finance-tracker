from flask import Flask, render_template


# Check in future, __name__ param can be buggy
app = Flask(__name__, template_folder="templates")


# list of dictionaries of expenses
expenses = []


@app.route("/")
def index():
    return render_template("index.html", expenses = expenses)


if __name__ == "__main__":
    app.run(debug=True)