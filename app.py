from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
users = {}

# ------------------------------
# GET - Retrieve all users
# ------------------------------
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


# ------------------------------
# GET - Retrieve a specific user by ID
# ------------------------------
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404


# ------------------------------
# POST - Add a new user
# ------------------------------
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = data
    return jsonify({"message": "User added", "user_id": user_id}), 201


# ------------------------------
# PUT - Update an existing user
# ------------------------------
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated"}), 200


# ------------------------------
# DELETE - Remove a user
# ------------------------------
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404


# ------------------------------
# Run the app
# ------------------------------
if __name__ == '__main__':
    app.run(debug=True)
