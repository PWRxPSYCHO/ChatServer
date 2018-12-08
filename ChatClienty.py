from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

msg_list = []
def receive():
    while True:
        try:
            msg = client_socket.recv(buffer_size).decode("utf8")
            msg_list.append(msg)
        except OSError:
            break



buffer_size = 1024
ADDR = ('localhost', 33000)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.start()