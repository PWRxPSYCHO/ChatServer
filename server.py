from threading import Thread
from socket import *
import queue


clients = []


def incoming_messages(serverSocket, client_messages):
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        client_messages.put((message, clientAddress))


def incoming_connections():
    serverPort = 5000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('localhost', serverPort))

    client_messages = queue.Queue()
    print("The server is ready to receive")

    Thread(target=incoming_messages, args=(
        serverSocket, client_messages)).start()

    while True:
        while not client_messages.empty():
            message, clientAddress = client_messages.get()
            if clientAddress not in clients:
                message = message.decode()
                message = message.split(':', 1)
                serverSocket.sendto(
                    ("Welcome to the server! %s Type !quit if you want to quit" % message[0]).encode(), clientAddress)
                for client in clients:
                    serverSocket.sendto(
                        (message[0] + " has joined the server.").encode(), client)
                clients.append(clientAddress)
                rint(message[0] + "has joined the server")
                continue
            message = message.decode()
            if "!quit" in message:
                clients.remove(clientAddress)
                message = message.split(':', 1)
                for client in clients:
                    serverSocket.sendto(
                        (message[0] + " has left the server.").encode(), client)
                print(message[0] + "has left the server")
                continue
            print(str(clientAddress) + message)
            for client in clients:
                if client != clientAddress:
                    serverSocket.sendto(message.encode(), client)
    serverSocket.close()


if __name__ == '__main__':
    incoming_connections()
