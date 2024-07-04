from fakeapi.traverse_json import traverse_json
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/health")
def health():
    return jsonify({"status": "OK"})


@app.route("/data", methods=["POST"])
def data():
    body = request.get_json()
    response = traverse_json(body)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)