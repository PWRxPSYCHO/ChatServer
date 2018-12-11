from socket import AF_INET, socket, SOCK_DGRAM
from threading import Thread

serverHost = ''
serverPort = 5000
addr = (serverHost, serverPort)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(addr)
#serverSocket.setblocking(0)

clients = []
isRunning = True
print('Server Started')

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
