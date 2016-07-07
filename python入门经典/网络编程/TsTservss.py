

from socketserver import (TCPServer as TCP,
     StreamRequestHandler as SRH)
from time import ctime

host = ''
port = 21567
addr = (host, port)

class MyRequestHandler(SRH):
    def handler(self):
        print ('...connected from:', self.client_address)
        self.wfile.write('[%s] %s'%(ctime(),
            self.rfile.readline()))

tcpServ = TCP(addr, MyRequestHandler)
print('waiting for connectiong...')
tcpServ.serve_forever()
