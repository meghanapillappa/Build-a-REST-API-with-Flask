from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage
users = {}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    if not data or "id" not in data or "name" not in data:
        return jsonify({"error": "Invalid data"}), 400
    users[data["id"]] = {"name": data["name"]}
    return jsonify({"message": "User added"}), 201

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    users[user_id].update(data)
    return jsonify({"message": "User updated"}), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
