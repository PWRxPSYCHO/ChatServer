from socket import *
from threading import Thread


serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

clients = {}


def incoming_connections():
    while True:
        clientMessage, clientAddress = serverSocket.recvfrom(2048)
        print("%s:%s has connected." % clientAddress)
        name_message = "Type your name: "
        serverSocket.sendto(name_message.encode(), clientAddress)
        Thread(target=handle_messages, args=(clientMessage,)).start()


def handle_messages(clientMessage):
    while True:
        clientMessage, clientAddress = serverSocket.recvfrom(2048)
        name = clientMessage.decode()
        clients[name] = clientAddress
        welcome_message = "Welcome to the server! Type !quit to exit."
        serverSocket.sendto(welcome_message.encode(), clientAddress)
        msg = "%s has joined!" % name
        broadcast((msg))


def broadcast(msg, prefix=""):
    for connections in clients:
        serverSocket.sendto((prefix + msg).encode(), connections)

if __name__ == "__main__":
    print("The server is ready to receive")
    INCOMING_CLIENTS = Thread(target=incoming_connections)
    INCOMING_CLIENTS.start()
    INCOMING_CLIENTS.join()