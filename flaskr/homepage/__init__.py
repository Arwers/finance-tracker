from flaskr.homepage.views import homepage


@homepage.context_processor
def utility_processor():
    def money_exceed(limit, total_cost):
        exceed = int(limit) - int(total_cost)
        if exceed < 0:
            return -exceed
        else:
            return 0

    def money_left(limit, total_cost):
        left = int(limit) - int(total_cost)
        if left > 0:
            return left
        else:
            return 0

    return dict(money_exceed=money_exceed, money_left=money_left)
