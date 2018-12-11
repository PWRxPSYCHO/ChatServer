from socket import *
import threading

serverHost = "localhost"
serverPort = 5000
isConnected = True


def incoming_messages(name, sock):
    while isConnected:
        while True:
            data, addr = sock.recvfrom(1024)
            print(data.decode())


serverSocket = socket(AF_INET, SOCK_DGRAM)
receiveThread = threading.Thread(
    target=incoming_messages, args=("ReceiveingThread", serverSocket))
receiveThread.start()

name = input("Enter your name: ")
message = input(name + ": ")

while message != "!quit":
    if message != '':
        serverSocket.sendto((name + ": " + message).encode(),
                            (serverHost, serverPort))

    message = input(name + ":")

isConnected = False
receiveThread.join()
serverSocket.close()
