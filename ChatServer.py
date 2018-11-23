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
        client.send(bytes("Hello! Welcome to the server! Type your username and press enter"))
        addresses[client] = address
        Thread(targer=handle_client, args=(client,)).start()

        