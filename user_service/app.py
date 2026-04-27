from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
#from flask_cors import CORS
#CORS(app)
SECRET = "secret"

users = []

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    return jsonify({"msg": "User created"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json

    for user in users:
        if user['username'] == data['username'] and user['password'] == data['password']:
            token = jwt.encode({
                'user': user['username'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, SECRET, algorithm="HS256")

            return jsonify({"token": token})

    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/delete', methods=['DELETE'])
def delete_user():
    token = request.headers.get('Authorization')

    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        username = decoded['user']

        global users
        users = [u for u in users if u['username'] != username]

        return jsonify({"msg": f"User {username} deleted"})
    except:
        return jsonify({"msg": "Invalid token"}), 401

@app.route('/profile', methods=['GET'])
def profile():
    token = request.headers.get('Authorization')

    try:
        decoded = jwt.decode(token, SECRET, algorithms=["HS256"])
        return jsonify({"user": decoded['user']})
    except:
        return jsonify({"msg": "Invalid token"}), 401

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(host='0.0.0.0')