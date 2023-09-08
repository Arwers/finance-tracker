def total_cost_count(expenses):
    total_cost = 0
    for item in expenses:
        total_cost += item["cost"]
    return total_cost

def set_all_costs(all_costs, expenses):
    for expense in expenses:
        all_costs[expense["category"]] += expense["cost"]
        all_costs["total"] += expense["cost"]
    return all_costs