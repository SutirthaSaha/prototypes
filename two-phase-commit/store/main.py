from flask import Flask, jsonify, request

from db import DB

app = Flask(__name__)
db = DB()


@app.route('/store/food/reserve', methods=['POST'])
def reserve_food_packet():
    food_id = request.json.get('foodId')
    packet_id = db.reserve_food_packet(food_id)
    return jsonify({"packetId": packet_id})


@app.route("/store/food/book", methods=["POST"])
def book_food_packet():
    packet_id = request.json.get('packetId')
    order_id = request.json.get('orderId')

    packet_id = db.book_food_packet(packet_id, order_id)
    return jsonify({"packetId": packet_id, "orderId": order_id})


if __name__ == "__main__":
    app.run(port=5002)
