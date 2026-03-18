from flask import Flask, jsonify
import json

app = Flask(__name__)
DATA_FILE = "data.json"

def read_data():
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return data

@app.route("/api", methods=["GET"])
def api():
    data = read_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

