from flaskr.homepage.utils import count_money_left
from flaskr.__init__ import app


def count_money_left(limit, total):
    temp = limit - total
    if temp < 0:
        return temp
    else:
        return 0

# !
app.jinja_env.globals.update(count_money_left = count_money_left)