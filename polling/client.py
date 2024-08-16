import requests
import time

base_url = "http://127.0.0.1:5000"


def short_poll():
    while True:
        response = requests.get(url=f"{base_url}/short-poll")
        response.raise_for_status()

        data = response.json()
        if data["status"] == "UP":
            print("The server is now up and running")
            break
        print("The server is down :(")
        time.sleep(3)


def long_poll():
    while True:
        try:
            response = requests.post(url=f"{base_url}/long-poll", json={
                'status': "DOWN"
            })
            response.raise_for_status()
            data = response.json()
            print(f"The server is now {data['status']}")
            break
        except Exception as e:
            print(f"Request failed with {e}")


if __name__ == "__main__":
    # short_poll()
    long_poll()
