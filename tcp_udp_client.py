from socket import *

def tcp_client():
    host = 'localhost'
    port = 12345
    addr = (host,port)
    bufsiz = 1024

    c = socket(AF_INET,SOCK_STREAM)
    c.connect(addr)

    while True:
        data = input('>')
        if not data:break
        c.send(data.encode())
        data_server = c.recv(bufsiz)
        if not data_server:break
        print(data_server.decode())
        #conn.close()
    c.close()

def udp_cli():
    port = 12345
    host = 'localhost'
    addr = (host, port)

    c = socket(AF_INET,SOCK_DGRAM)
    c.connect(addr)

    while True:
        data = input('>')
        if not data:break
        c.sendto(data.encode(),addr)
        data_from_ser,addre = c.recvfrom(1024)
        if not data_from_ser:break
        print(data_from_ser.decode())
        #print('decode():',data_from_ser.decode())
    c.close()

if __name__ == '__main__':
    udp_cli()