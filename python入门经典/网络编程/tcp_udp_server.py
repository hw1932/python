#coding=utf-8
from socket import *
import time


def tcp_server():
    host = ''
    port = 12345
    addr = (host, port)
    bufsiz = 1024

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(addr)
    s.listen(5)

    while True:
        print('\nwaiting connecting')
        conn,addre = s.accept()
        print('get connection from ',addre)
        while True:
            data = conn.recv(bufsiz)
            if not data:break
            print('client data->',data.decode())
            conn.send(b'this is server')
            #conn.close()
    s.close()

def udp_ser():
    host = ''
    port = 12345
    addr = (host,port)

    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(addr)

    while True:
        print('wait for connecting')
        data,addre = s.recvfrom(1024)
        if not data:break
        print('client data.decode()->',data.decode())
        print('client data->',data)
        data_to_cli = time.ctime()+'你好'
        s.sendto(data_to_cli.encode(),addre)
    s.close()



if __name__ == '__main__':
    udp_ser()