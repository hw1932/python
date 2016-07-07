#coding=utf-8
import socket

def server():
    s = socket.socket()
    host =  socket.gethostname()
    port = 1234
    s.bind((host,port))
    s.listen(5)

    while True:
        c,addr = s.accept()
        print('get connect from %s '%addr)
        c.send('thank you for connecting')
        content = c.recv(1024)
        print(content)
        c.close()

if __name__ == '__main__':
    server()
