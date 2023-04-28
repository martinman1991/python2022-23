class klassz:
    x=5
    def megnovel(self,mennyivel=1):
        self.x+=mennyivel

class kutya:
    nev,fajta,agresszivitas,kor,szin=["","",0,0,""]
    def __init__(self,nev,fajta,agresszivitas,kor,szin):
        self.nev=nev
        self.fajta=fajta
        self.agresszivitas=agresszivitas
        self.kor=kor
        self.szin=szin

    def ugat(self):
        print("*ugatás hangok*")

    def koszon(self):
        print("Vau-vau, {} vagyok".format(self.nev))

    def talalkozas(self,masik):
        if self.agresszivitas>5 or masik.agresszivitas>5:
            #támadás
            if self.agresszivitas>=masik.agresszivitas:
                print("Megöllek, gugya!")
            else:
                print("Nebánncs báttya!")
        else:
            if self.agresszivitas>=masik.agresszivitas:
                print("Szia uram")
            else:
                print("Zilya gutya")
    def __str__(self):
        return "{},{},({})".format(self.nev,self.fajta,self.kor)

class kotorek(kutya):
    def koszon(self):
        print("{} a nevem, kutyaság a mindenem".format(self.nev))
    def __init__(self,nev,fajta,agresszivitas,kor,szin,szemszin):
        super().__init__(nev,fajta,agresszivitas,kor,szin)
        self.szemszin=szemszin

k1=kutya("Bodri","Puli",3,9,"felete")
k2=kutya("Morzsi","golden retriever",1,3,"világos barna")

k1.ugat()
k1.koszon()
k2.koszon()

k2.talalkozas(k1)
k1.talalkozas(k2)

print(klassz.x)

p1=klassz()
print(p1.x)
p2=klassz()
p2.x=1
print(p2.x)

p1.megnovel()
p1.megnovel(10)

print(p1.x)

kotor1=kotorek("Füles","tacskó",10,4,"barna","zöld")
kotor1.koszon()
k1.talalkozas(kotor1)
print(kotor1.szemszin)
print(kotor1)
print(k1)
