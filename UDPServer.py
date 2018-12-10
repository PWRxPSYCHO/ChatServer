from socket import *
from threading import Thread


serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

clients = []

print('Server Started')

while True:
        try:
                data, addr = serverSocket.recvfrom(2048)
                if "!quit" in str(data):
                        break
                if addr not in clients:
                        clients.append(addr)
                print(str(addr) + ":" + str(data))
                for client in clients:
                        serverSocket.sendto(data, client)
        except:
                pass
serverSocket.close()
