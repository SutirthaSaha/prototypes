import threading

import requests

delivery_url = "http://localhost:5001"
store_url = "http://localhost:5002"


def place_order(food_id):
    try:
        # reserve packet
        response = requests.post(f"{store_url}/store/food/reserve", json={"foodId": food_id})
        response.raise_for_status()
        response_json = response.json()

        packet_available = response_json["packetId"]

        # reserve agent
        response = requests.post(f"{delivery_url}/delivery/agent/reserve")
        response.raise_for_status()
        response_json = response.json()

        agent_available = response_json["agentId"]

        # book agent
        response = requests.post(f"{delivery_url}/delivery/agent/book", json={"agentId": agent_available})
        response.raise_for_status()
        response_json = response.json()

        # book packet
        response = requests.post(f"{store_url}/store/food/book", json={"packetId": packet_available})
        response.raise_for_status()
        response_json = response.json()

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    threads = []
    num = 1
    food_id = 1
    for _ in range(num):
        thread = threading.Thread(target=place_order, args=(food_id,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
