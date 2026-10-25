import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5050))
server.listen(1)

print("Server is waiting for a connection...")

connection, address = server.accept()
print("Client connected!")

while True:
    message = connection.recv(1024).decode()

    if message.lower() == "quit":
        print("Client ended the chat.")
        break

    print("Client:", message)

    reply = input("You: ")
    connection.send(reply.encode())

    if reply.lower() == "quit":
        break

connection.close()
server.close()