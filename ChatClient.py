import socket
import threading
host = 'localhost'
port = '5000'


# Client Code
def Server_Message(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print(data.decode())
        except:
            pass


def RunClient():
    server = ((addr), port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #s.bind(('', port))

    name = input('Please write your name here: ')
    print('Your name is:'+name)
    s.sendto(name.encode(), addr)
    threading.Thread(target=Server_Message, args=(s,)).start()
    while True:
        data = input()
        if data == '!quit':
            break
        elif data == '':
            continue
        data = '['+name+']' + '->' + data
        s.sendto(data.encode('utf-8'), addr)
    s.sendto(data.encode('utf-8'), addr)


if __name__ == '__main__':
    RunClient()
