
def total_cost_count(expenses):
    total_cost = 0
    for item in expenses:
        total_cost += item["cost"]
    return total_cost
