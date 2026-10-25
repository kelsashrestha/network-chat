import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 5050))

print("Connected to the server!")

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == "quit":
        break

    reply = client.recv(1024).decode()

    if reply.lower() == "quit":
        print("Server ended the chat.")
        break

    print("Server:", reply)

client.close()