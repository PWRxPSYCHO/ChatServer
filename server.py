from threading import Thread
from socket import *
import queue


clients = []
leaveClient = []
joinClient = []


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
                joinClient.append(message[0])
                for client in clients:
                    serverSocket.sendto(
                        (joinClient[0] + " has joined the server.").encode(), client)
                joinClient.pop()

                clients.append(clientAddress)
                continue
            message = message.decode()
            if "!quit" in message:
                clients.remove(clientAddress)
                message = message.split(':', 1)
                leaveClient.append(message[0])
                for client in clients:
                    serverSocket.sendto(
                        (leaveClient[0] + " has left the server.").encode(), client)
                leaveClient.pop()
                continue
            print(str(clientAddress) + message)
            for client in clients:
                if client != clientAddress:
                    serverSocket.sendto(message.encode(), client)
    serverSocket.close()


if __name__ == '__main__':
    incoming_connections()
