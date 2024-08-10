import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific host and port
server_socket.bind(("localhost", 12345))

# Enable the server to accept connections
server_socket.listen()

print("Server is listening...")

# Accept a connection
client_socket, address = server_socket.accept()

print(f"Connection from {address} has been established.")

while True:
    # Receive message from client
    message = client_socket.recv(1024).decode("utf-8")
    print(f"Client: {message}")

    # Send message to client
    server_message = input("Server: ")
    client_socket.send(server_message.encode("utf-8"))

client_socket.close()
