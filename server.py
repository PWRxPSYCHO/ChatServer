from threading import Thread
from socket import *
import queue


clients = []


def incoming_messages(serverSocket, client_messages):
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        client_messages.put((message, clientAddress))


def incoming_connections():
    #setup server
    serverPort = 5000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('localhost', serverPort))

    #adds incoming messages to a Queue to be processed later
    client_messages = queue.Queue()
    print("The server is ready to receive")

    Thread(target=incoming_messages, args=(
        serverSocket, client_messages)).start()

        #main loop, makes sure the queue isn't empty
    while True:
        while not client_messages.empty():
            message, clientAddress = client_messages.get()
            #checks if a new connection if so add them to list of connections, send welcome message and alert all users that they joined
            if clientAddress not in clients:
                message = message.decode()
                name = message.split(':', 1)
                serverSocket.sendto(
                    ("Welcome to the server! %s Type !quit if you want to quit" % name[0]).encode(), clientAddress)
                for client in clients:
                    serverSocket.sendto(
                        (name[0] + " has joined the server.").encode(), client)
                clients.append(clientAddress)
                print(name[0] + " has joined the server")
                continue
            message = message.decode()
            #checks if the user wants to exit, if they do send message to other users that client has left
            if "!quit" in message:
                clients.remove(clientAddress)
                name = message.split(':', 1)
                for client in clients:
                    serverSocket.sendto(
                        (name[0] + " has left the server.").encode(), client)
                print(name[0] + " has left the server")
            print(str(clientAddress) + message)
            #sends message to all clients
            for client in clients:
                if clientAddress not in clients:
                    break
                if client != clientAddress:
                    serverSocket.sendto(message.encode(), client)
    serverSocket.close()


if __name__ == '__main__':
    incoming_connections()
