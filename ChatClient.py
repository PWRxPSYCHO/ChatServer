from socket import *
import threading

serverHost = "localhost"
serverPort = 5000
threadLock = threading.Lock()
isConnected = True


def incoming_messages(name, sock):
    while isConnected:
        try:
            threadLock.acquire()
            while True:
                data, addr = socket.recvfrom(2048)
                print(str(data))
        except:
            pass
        finally:
            threadLock.release()


serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

receiveThread = threading.Thread(
    target=incoming_messages, args=("ReceiveingThread", serverSocket))
receiveThread.start()

name = input("Enter your name: ")
message = input(name + ": ")

while message != "!quit":
    if message != '':
        serverSocket.sendto(name + ": " + message, (serverHost, serverPort))
    threadLock.acquire()
    message = input(name + "->")
    threadLock.release()

isConnected = False
receiveThread.join()
serverSocket.close()
