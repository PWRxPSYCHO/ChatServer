from socket import AF_INET, socket, SOCK_STREAM
import threading

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
print("The server is ready to receive")

clients = {}
addresses = {}


def handle_client(connection_socket):
    name = connection_socket.recv(1024).decode()
    welcome_message = "Welcome %s. To exit, type Quit." % name
    connection_socket.send(welcome_message).encode()
    message = "%s has joined!" % name
    broadcast(bytes(message, "utf8"))
    clients[connection_socket] = name

    while True:
        message = connection_socket.recv(1024).decode()
        if message != "Quit":
            broadcast(message, name+": ")
        else:
            connection_socket.send(message.encode())
            connection_socket.close()
            del clients[connection_socket]
            broadcast(bytes("%s has left the chat" % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for connections in clients:
        connections.send(bytes(prefix, "utf8")+msg)


class ServiceThread(threading.Thread):
    def __init__(self, connection_socket):
        threading.Thread.__init__(self)
        self.connection_socket = connection_socket

    def run(self):
        handle_client(self.connection_socket)


while True:
    connection_socket, addr = serverSocket.accept()
    print("%s:%s has connected" % addr)
    connection_socket.send("Type your name: ").encode()
    addresses[connection_socket] = addr
    new_thread = ServiceThread(connection_socket)
    new_thread.start()
