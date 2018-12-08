from socket import *

serverName = 'localhost'
serverPort = 6000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    message = input("Enter your username:")
    clientSocket.send(message.encode())
    if message == "Quit":
        break
    else:
        modifiedSentence = clientSocket.recv(1024)
        print(modifiedSentence.decode())