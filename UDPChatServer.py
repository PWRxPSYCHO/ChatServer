from socket import *
from threading import Thread

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))


print("The server is ready to receive")
message, clientAddress = serverSocket.recvfrom(2048)

clients = {}


def init_connection():
    while True:
        print("%s:%s has connected" % clientAddress)
        serverSocket.sendto(("Type your name: ").encode(), clientAddress)
        Thread(target=handle_client, args=(serverSocket,)).start()


def handle_client(serverSocket):
    name = message.decode()
    clients[name] = clientAddress
    welcome_message = "Welcome %s. To exit, type !quit." % name
    serverSocket.sendto(welcome_message.encode(), clientAddress)
    msg = "%s has joined!" % name
    broadcast((msg))

    while True:
        client_message = message.decode()
        if client_message != "!quit":
            broadcast(client_message, name+":")
        else:
            serverSocket.sendto(("!quit").encode(), clientAddress)
            serverSocket.close()
            del clients[name]
            broadcast(("%s has left the chat" % name))
            break


def broadcast(msg, prefix=""):

    for connections in clients:
        connections.sendTo((prefix + msg).encode(), connections)


if __name__ == "__main__":
    print("The server is ready to receive")
    ACCEPT_THREAD = Thread(target=clientAddress)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverSocket.close()
