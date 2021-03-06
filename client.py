from socket import *
from threading import Thread

serverName = 'localhost'
serverPort = 5000
isRunning = True

clientSocket = socket(AF_INET, SOCK_DGRAM)


def server_messages(socket):
    while True:
        try:
            data, addr = socket.recvfrom(2048)
            print(data.decode())
        except:
            pass


def client_main():
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    #gets username from client
    username = input("Enter your username: ")

    serverSocket.sendto(username.encode(), (serverName, serverPort))
    Thread(target=server_messages, args=(serverSocket,)).start()

#allows user to send message and checks if they want to quit.
    while isRunning:
        message = input("")
        if "!quit" in message:
            isRunning == False
            message = username + ": " + message
            serverSocket.sendto(message.encode(), (serverName, serverPort))
            serverSocket.close()
            break
        message = username + ": " + message
        serverSocket.sendto(message.encode(), (serverName, serverPort))
    serverSocket.close()


if __name__ == '__main__':
    client_main()
