def test_hello():
    from app import app
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert response.data.decode() == 'Hello, World!'