from threading import Thread
from socket import *
import queue

print("The server is ready to receive")

clients = []


def incoming_messages(serverSocket, client_messages):
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        client_messages.put((message, clientAddress))


def incoming_connections():
    serverPort = 5000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    client_messages = queue.Queue()

    while True:
        data, addr = client_messages.get()
        if addr not in clients:
            clients.append(addr)
            continue
        clients.append(addr)
        data = data.decode()
        if "!quit" in data.decode():
            clients.remove(addr)
            continue
        print(str(addr) + ": " + data)
        for client in clients:
            if client != addr:
                serverSocket.sendto(data.encode(), client)

    Thread(target=incoming_messages, args=(
        serverSocket, client_messages)).start()
    serverSocket.close()


if __name__ == '__main__':
    incoming_connections()
