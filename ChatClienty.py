from socket import *
from threading import Thread

serverName = 'localhost'
serverPort = 5000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def incoming_messages():
    while True:
        try:
            message = clientSocket.recv(1024)
            print(message.decode())
        except OSError:
            break


def client_messages():
    clientMsg = input("")
    clientSocket.send(clientMsg.encode())
    if clientMsg == "quit":
        clientSocket.close()


if __name__ == "__main__":
    receive_thread = Thread(target=incoming_messages)
    receive_thread.start()
