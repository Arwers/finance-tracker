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
