from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))


clients = {}
addresses = {}


def client_connections():
    while True:
        connection_socket, addr = serverSocket.accept()
        print("%s:%s has connected" % addr)
        connection_socket.send(bytes("Type your name: ", "utf8"))
        addresses[connection_socket] = addr
        Thread(target=handle_client, args=(connection_socket,)).start()


def handle_client(connection_socket):
    name = connection_socket.recv(1024).decode()
    welcome_message = "Welcome %s. To exit, type Quit." % name
    connection_socket.send(bytes(welcome_message, "utf8"))
    message = "%s has joined!" % name
    broadcast(bytes(message, "utf8"))
    clients[connection_socket] = name

    while True:
        message = connection_socket.recv(1024).decode()
        if message != bytes("Quit", "utf8"):
            broadcast(message, name+": ")
        else:
            connection_socket.send(bytes(message, "utf8"))
            connection_socket.close()
            del clients[connection_socket]
            broadcast(bytes("%s has left the chat" % name, "utf8"))
            break


def broadcast(msg, prefix=""):
    for connections in clients:
        connections.send(bytes(prefix, "utf8")+msg)


if __name__ == "__main__":
    serverSocket.listen(5)
    print("The server is ready to receive")
    ACCEPT_THREAD = Thread(target=client_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverSocket.close()
