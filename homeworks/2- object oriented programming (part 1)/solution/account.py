class Account:
    def __init__(self,name):
        self.money = 0
        self.trankesh = []
        self.name = name
    def addMoney(self,x,s):
        z = []
        z.append(x)
        z.append(s)
        self.money += x
        self.trankesh.append(z)
    def subMoney(self,x,s):
        z = []
        z.append(-x)
        z.append(s)
        self.money -= x
        self.trankesh.append(z)
    def __str__(self):
        return "name: "+self.name+" money: "+str(self.money)
    def print_all_transactions(self):
        for i in self.trankesh:
            print i[1]+' '+str(i[0])

a = Account('sajad')
print a
a.addMoney(100,'jayeze')
print a
a.subMoney(100,'jayeze')
a.print_all_transactions()
