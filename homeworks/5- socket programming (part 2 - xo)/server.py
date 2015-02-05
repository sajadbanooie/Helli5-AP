__author__ = 'sajad'
import xolib

server = xolib.Xoserver(('localhost',5001))
print server.accept('x')
print 'x joind'
print server.accept('o')
print 'y joind'
map = [[0,0,0],[0,0,0],[0,0,0]]
server.sendmap(map)
s = 0
i = 1
while 1:
    if s==-1:
        server.o.send('wi')
        server.x.send('l')

        break
    elif s==1:
        server.o.send('l')
        server.x.send('wi')

        break
    elif s==1:
        server.o.send('d')
        server.x.send('d')

        break
    elif i%2==1:
        server.x.send('r')
        server.o.send('w')
        index = server.x.recv(1024)
        v = 1

    elif i%2==0:
        server.x.send('w')
        server.o.send('r')
        index = server.o.recv(1024)
        v = -1

    index1,index2 = index.split(',')
    if map[int(index1)][int(index2)]==0:
        map[int(index1)][int(index2)] = v
        i += 1
    s = xolib.wdl(map)
    server.sendmap(map)


server.close()