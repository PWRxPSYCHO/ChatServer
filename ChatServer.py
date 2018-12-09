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
    welcome_message = "Welcome %s. To exit, type !quit." % name
    connection_socket.send(bytes(welcome_message, "utf8"))
    message = "%s has joined!" % name
    broadcast((message))
    clients[connection_socket] = name

    while True:
        message = connection_socket.recv(1024).decode()
        if message != "!quit":
            broadcast(message, name+": ")
        else:
            connection_socket.send(bytes("!quit","utf8"))
            connection_socket.close()
            del clients[connection_socket]
            broadcast(("%s has left the chat" % name))
            break


def broadcast(msg, prefix=""):

    for connections in clients:
       connections.send((prefix + msg).encode())


if __name__ == "__main__":
    serverSocket.listen(5)
    print("The server is ready to receive")
    ACCEPT_THREAD = Thread(target=client_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    serverSocket.close()
