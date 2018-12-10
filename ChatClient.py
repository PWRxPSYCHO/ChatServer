from socket import *
from threading import Thread

serverName = 'localhost'
serverPort = 5000

clientSocket = socket(AF_INET, SOCK_DGRAM)


def incoming_messages():
    while True:
        try:
            message, serverAddress = clientSocket.recvfrom(2048)
            print(message.decode())
        except OSError:
            break


def client_messages():
    clientMsg = input("")
    clientSocket.sendto(clientMsg.encode(), (serverName, serverPort))
    if clientMsg == "!quit":
        clientSocket.close()


if __name__ == "__main__":
    receive_thread = Thread(target=incoming_messages)
    receive_thread.start()
    while True:
        client_messages()
