from socket import *

client = socket(AF_INET,SOCK_STREAM)

client.connect(('localhost',5050))

i = 1
while 1:
    x = raw_input()
    client.send(x)
    if i %2 == 0:
        data = client.recv(1024)
        print data

    i += 1
