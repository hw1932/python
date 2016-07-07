from socket import *

host = 'localhost'
port = 21567
bufsiz = 1024
addr = (host,port)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(addr)

    data = input('>')
    if not data:
        break
    tcpCliSock.send(('%s\r\n'%data).encode())

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(addr)
    data = tcpCliSock.recv(bufsiz)
    if not data:
        break
    print (data.strip())

    tcpCliSock.close()