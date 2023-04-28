class telek:
    paros=False
    szelesseg=0
    kerites=""

    def __init__(self,sor):
        vag=sor.replace("\n","").split(" ")
        print(vag)
        if vag[0]==1:
            paros=False
        else:
            paros=True

        self.paros=vag[0]==0

        self.szelesseg=int(vag[1])

        self.kerites=vag[2]
    
f=open("kerites.txt")
for sor in f:
    print(sor)

f.close()
