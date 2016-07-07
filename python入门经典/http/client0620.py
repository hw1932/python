#coding=utf-8
import socket

def client():
    s = socket.socket()
    host = socket.gethostname()#server()中服务器的IP，不是自己的，这里是C/S都在本机
    port = 123     #server()中服务器的port，不是客户端自己的
    s.connect((host,port))
    s.send('this is client')
    print('%s' %s.recv(1024))
    s.close()

if __name__ == '__main__':
    client()