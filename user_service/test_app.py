from user_service.app import app, users

def test_register():
    users.clear()
    client = app.test_client()

    payload = {
        "username": "Ivan",
        "password": "0123456789"
    }

    response = client.post('/register', json=payload)

    assert response.status_code == 201
    assert response.get_json()["msg"] == "User created"
    assert users[-1]["username"] == "Ivan"