from socket import *

serverName = 'localhost'
serverPort = 5000

clientSocket = socket(AF_INET, SOCK_DGRAM)
print("Type !quit when you want to exit ")

while True:
    message = input("Name: ")
    if ("!quit" in message):
        break
    else:
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode())

