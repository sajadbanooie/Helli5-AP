from socket import *

server = socket(AF_INET,SOCK_STREAM)

server.bind(('localhost',5050))

server.listen(5)

while 1:
    client,adress = server.accept()
    print 'client joined from',adress
    break

i = 1
x = 0
while 1:
    data = client.recv(1024)
    y = int(data)
    if i%2==0:
        client.send( str( x + y ) )
    x = int(data)
    i +=1
