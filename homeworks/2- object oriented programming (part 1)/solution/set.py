class Set:
    def __init__(self):
        self.list = []
    def append(self,a):
        if a not in self.list:
            self.list.append(a)
    def remove(self,x):
        if x in self.list:
            self.list.remove(x)
        else:
            print 'not found'
    def size(self):
        return len(self.list)
