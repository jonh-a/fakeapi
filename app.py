from traverse_json import traverse_json
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({ "status": "OK" })


@app.route("/data", methods=["POST"])
def data():
    body = request.get_json()
    response = traverse_json(body)
    return jsonify(response) 


if __name__ == "__main__":
    app.run(debug=True)