from app import register

def test_register():
    data = {"username": "test", "password": "test"}
    response = register(data)
    assert response.status_code == 201