from flask import Flask, jsonify, request
import json
import time

app = Flask(__name__)
timeout = 15


def get_status():
    with open("data.json", "r") as f:
        data = json.load(f)
        status = data["status"]
    return status


@app.route('/short-poll', methods=['GET'])
def short_poll():
    print("Hello")
    return jsonify({"status": get_status()})


@app.route('/long-poll', methods=['POST'])
def long_poll():
    curr_status = request.json.get('status')
    status = get_status()
    while status == curr_status:
        time.sleep(2)
        status = get_status()

    return jsonify({"status": get_status()})


if __name__ == "__main__":
    app.run(port=5000)
