from threading import Thread
from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("The server is ready to receive")

clients = []


def incoming_messages():
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
    if clientAddress not in clients:
        clients.append(clientAddress)
    message = message.decode()
    print(message)
    for client in clients:
        serverSocket.sendto(message, clientAddress)

    Thread(target=incoming_messages, args=(serverSocket, message)).start()
