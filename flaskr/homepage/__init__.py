from flaskr import app

def count_money_left(limit, total):
    temp = limit - total
    if temp < 0:
        return temp
    else:
        return 0

app.jinja_env.globals.update(count_money_left = count_money_left)