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
                clients.append(clientAddress)
                continue
            message = message.decode()
            if "!quit" in message:
                clients.remove(clientAddress)
                for client in clients:
                    serverSocket.sendto(
                        (clientAddress + " has left the server.").encode(), client)
                continue
            print(str(clientAddress) + message)
            for client in clients:
                if client != clientAddress:
                    serverSocket.sendto(message.encode(), client)
    serverSocket.close()


if __name__ == '__main__':
    incoming_connections()
