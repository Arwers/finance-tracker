def test_total_cost_count():
    """Test that the total cost is calculated correctly."""
    from flaskr.home.utils import total_cost_count

    expenses = [
        {"cost": 10.2},
        {"cost": 20.1},
        {"cost": 0},
        {"cost": 40},
        {"cost": 50},
    ]
    assert total_cost_count(expenses) == 120.3
