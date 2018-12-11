from socket import AF_INET, socket, SOCK_DGRAM
from threading import Thread

serverHost = ''
serverPort = 5000
addr = (serverHost, serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(addr)
serverSocket.setblocking(0)

clients = []
isRunning = True
print('Server Started')

while isRunning:
    try:
        data, addr = serverSocket.recvfrom(2048)
        message = data.decode()
        address = addr.decode()
        if "!quit" in message:
            isRunning = False
        if addr not in clients:
            clients.append(address)
        print(address + ":" + message)
        for client in clients:
            serverSocket.sendto(data, client)
    except:
        pass
serverSocket.close()
