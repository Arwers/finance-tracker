def total_cost_count(expenses):
    total_cost = 0
    for item in expenses:
        total_cost += item["cost"]
    return total_cost


def count_money_left(limit, total):
    temp = limit - total
    if temp < 0:
        return temp
    else:
        return 0