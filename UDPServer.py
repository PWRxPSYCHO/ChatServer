from socket import AF_INET, socket, SOCK_DGRAM
from threading import Thread
import queue

clients = []
isRunning = True

""" print('Server Started')

while isRunning:
    data, addr = serverSocket.recvfrom(1024)
    if "!quit" in str(data):
        isRunning = False
    if addr not in clients:
        clients.append(addr)
    print(str(addr) + ":" + str(data))
    for client in clients:
        serverSocket.sendto(data, client)
serverSocket.close()
 """


def Incoming_Messages(sock, messages):
    while isRunning:
        data, addr = sock.recvfrom(2048)


def running():
    serverHost = ''
    serverPort = 5000
    addr = (serverHost, serverPort)
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(addr)
    messages = queue.Queue()
    print('Server Started')
    Thread(target=Incoming_Messages, args=(serverSocket, messages)).start()

    while isRunning:
        data, addr = messages.get()
        if addr not in clients:
            clients.append(addr)
        data = data.decode()
        if "!quit" in data:
            clients.remove(addr)
        for client in clients:
            if client != addr:
                serverSocket.sendto(data.encode(), client)


if __name__ == '__main__':
    running()
