import socket

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("localhost", 12345))

while True:
    # Send message to server
    client_message = input("Client: ")
    client_socket.send(client_message.encode("utf-8"))

    # Receive message from server
    message = client_socket.recv(1024).decode("utf-8")
    print(f"Server: {message}")

client_socket.close()
