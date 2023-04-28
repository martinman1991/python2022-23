class muvelet:
    szam1=0
    szam2=0
    def __init__(self,szam1,szam2):
        self.szam1=szam1
        self.szam2=szam2

    def osszeadas(self):
        return self.szam1+self.szam2

    def kivonas(self):
        return self.szam1-self.szam2

    def zorzas(self):
        return self.szam1*self.szam2

    def osztas(self):
        return self.szam1/self.szam2
    
    #test
    q=muvelet(10,10)
    print(q.osszeadas())
    print(q.kivonas())
    print(q.zorzas())
    print(q.osztas())
