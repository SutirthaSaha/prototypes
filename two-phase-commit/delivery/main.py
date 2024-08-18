from flask import Flask, jsonify, request

from db import DB

app = Flask(__name__)
db = DB()


@app.route('/delivery/agent/reserve', methods=['POST'])
def reserve_delivery_agent():
    agent_id = db.reserve_delivery_agent()
    return jsonify({"agentId": agent_id})


@app.route("/delivery/agent/book", methods=["POST"])
def book_delivery_agent():
    agent_id = request.json.get('agentId')
    order_id = request.json.get('orderId')

    agent_id = db.book_delivery_agent(agent_id, order_id)
    return jsonify({"agentId": agent_id, "orderId": order_id})


if __name__ == "__main__":
    app.run(port=5001)
