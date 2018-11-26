from socket import *
from threading import Thread

clients = {}
addresses = {}

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
print("The server is ready to receive")


def incoming_clients():
    while True:
        client, address = serverSocket.accept()
        print("%s has connected" % address)
        client.send(
            bytes("Hello! Welcome to the server! Type your username and press enter"))
        addresses[client] = address
        Thread(targer=handle_client, args=(client,)).start()
        print("hello world")


def handle_client():
    print("This function will handle each individual client")
    print("Hello World")


if __name__ == "__main__":
    serverSocket.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=incoming_clients)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverSocket.close()
