__author__ = 'sajad'
import socket

class Xoserver(socket.socket):
    def __init__(self,host):
        super(Xoserver, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.x = None
        self.o = None
        self.bind(host)
        self.listen(5)
    def accept(self, t):
        c , a = super(Xoserver, self).accept()
        self.__setattr__(t, c)
        return a
    def sendmap(self,map):
        strmap = tostr(map)
        print strmap
        self.x.send(strmap)
        self.o.send(strmap)

class Xoclient(socket.socket):
    def __init__(self,host):
        super(Xoclient, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.connect(host)
    def recvmap(self):
        m = self.recv(2048)
        return m

def tostr(self):
    s = ''
    for i in self:
        for j in i:
            if j==1:
                s += 'X'
            if j==-1:
                s += 'O'
            if j==0:
                s += '#'
        s += '\n'
    return s

def wdl(map):
    s = 0
    for i in map:
        if 0 not in i:
            s = 10
        else:
            s = 0
    for i in map:
        if i[0]==i[1] and i[1]==i[0] and i[2]==i[0]:
            s=i[0]

    for i in range(len(map)):
        if map[0][i]==map[1][i] and map[1][i]==map[2][i] and map[2][i]==map[0][i]:
                s=map[0][i]

    if map[0][0]==map[1][1] and map[1][1]==map[2][2] and map[2][2]==map[0][0]:
        s=map[0][i]
    if map[0][2]==map[1][1] and map[1][1]==map[2][0] and map[2][0]==map[0][2]:
        s=map[0][i]

    print s
    return s




