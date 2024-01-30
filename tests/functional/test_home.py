def test_homepage(client):
    """Test homepage loads correctly."""
    response = client.get("/")
    assert response.status_code == 200
