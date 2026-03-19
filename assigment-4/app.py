from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://kc:2104@cluster0.0ziro8a.mongodb.net/?appName=Cluster0/to-do"
mongo = PyMongo(app)

@app.route('/')
def todo_page():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if not item_name or not item_description:
        return jsonify({"error": "Missing fields"}), 400

    mongo.db.todos.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({"message": "To-Do Item saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)

