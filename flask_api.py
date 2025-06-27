from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

user_info = {
    1: {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    2: {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"}
}

@app.route("/user_info", methods =["GET"])
def get_user_data():
    user_id = request.args.get("user_id", type=int)
    
    if user_id is None:
        return jsonify(list(user_info.values())), 200
    
    user = user_info.get(user_id)

    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route("/user_info", methods = ["POST"])
def create_user():
    request_data = request.get_json()
    if request_data:
        # Process the received JSON data
        new_user = {"id": len(user_info) + 1, "name": request_data["name"], "email": request_data["email"]}
        user_info[new_user["id"]] = new_user
        return jsonify(new_user), 201

    else:
        return jsonify({"error": "No valid JSON data received"}), 400
    
@app.route("/user_info", methods = ["DELETE"])
def remove_user():
    user_id = request.args.get("user_id", type=int)
    user = user_info.get(user_id)
    if user:
        del user_info[user_id]
        return jsonify({"message": f"Item {user} deleted successfully"}), 200
    else:
        return jsonify({"error": f"Item {user} not found"}), 404

@app.route("/user_info", methods=["PUT"])
def update_user():
    user_id = request.args.get("user_id", type=int)
    if user_id is None:
        return jsonify({"error": "Missing user_id parameter"}), 400

    user = user_info.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    user.update({k: v for k, v in data.items() if k in ["name", "email"]})
    return jsonify({"message": "User updated successfully", "user": user}), 200
if __name__ == "__main__":
    app.run(debug=True)