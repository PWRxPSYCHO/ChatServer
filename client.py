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
    #serverSocket.bind(('', serverPort))
    print("Welcome to the server! Type !quit when you want to quit.")

    username = input("Enter your username: ")
    print("Hello %s!" % username)

    serverSocket.sendto(username.encode(), (serverName, serverPort))
    Thread(target=server_messages, args=(serverSocket,)).start()

    while isRunning:
        message = input("")
        if "!quit" in message:
            break
        message = username + ": " + message
        serverSocket.sendto(message.encode(), (serverName, serverPort))
    serverSocket.close()

if __name__ == '__main__':
    client_main()
