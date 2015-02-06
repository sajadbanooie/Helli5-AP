__author__ = 'sajad'
import xolib
import os

client = xolib.Xoclient(('localhost', 5001))
map = client.recvmap()
print map
while 1:
    status = client.recv(1024)
    if status=='r':
        print 'enter the row and col:'
        x,y = input()
        client.send(str(x+1)+','+str(y+1))
    elif status=='w':
        print 'wait for the opponoment'
    elif status=='wi':
        print 'oh! you won'
        break
    elif status=='l':
        print 'oh! you have lost'
        break
    elif status=='d':
        print 'the game was a draw'
        break
    map = client.recvmap()
    print map
    os.system('cls')


client.close()
