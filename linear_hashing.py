class hash:
    def __init__(self,h1):
        self.h = h1
        self.table = []
        self.table = [[] for x in range (self.h)]

    def insrt(self,element):
        indx = element%self.h
        self.table[indx].append(element)
        print(self.table,len(self.table))
    def rmv(self,value):
        x = value%self.h
        if value in self.table[x]:
            self.table[x].remove(value)
            print(self.table,len(self.table))
        else:
            print('Value is not present')

    def srch(self,value):
        z = value%self.h
        if value in self.table[z]:
            return True
        else:
            return False


c1 = hash(7)
c1.insrt(7)
c1.insrt(14)
c1.insrt(70)
c1.insrt(71)
c1.insrt(9)
c1.insrt(56)
c1.insrt(72)
c1.rmv(10)
print(c1.srch(14))