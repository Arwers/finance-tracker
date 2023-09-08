from flaskr.homepage.views import homepage

@homepage.context_processor
def utility_processor():
    def money_exceed(limit, total_cost):
        temp = limit - total_cost
        if temp < 0:
            return temp
        else:
            return 0
