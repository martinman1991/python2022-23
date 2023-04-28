class orszag():
    def __init__(self,orszag):
        self.orszag=orszag

class torzs(orszag):
    def __init__(self,orszag,torzs):
        super().__init__(orszag)
        self.torzs=torzs

class altorzs(torzs):
    def __init__(self,orszag,torzs,altorzs):
        super().__init__(orszag,torzs)
        self.altorzs=altorzs

class foosztaly(altorzs):
    def __init__(self,orszag,torzs,altorzs,foosztaly):
        super().__init__(orszag,torzs,altorzs)
        self.foosztaly=foosztaly

class osztaly(foosztaly):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly):
        super().__init__(orszag,torzs,altorzs,foosztaly)
        self.osztaly=osztaly

class alosztaly(osztaly):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly)
        self.alosztaly=alosztaly

class alosztalyag(alosztaly):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly)
        self.alosztalyag=alosztalyag

class oregrend(alosztalyag):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag)
        self.oregrend=oregrend

class rend(oregrend):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend)
        self.rend=rend

class alrend(rend):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend)
        self.alrend=alrend

class csalad(alrend):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend)
        self.csalad=csalad

class alcsalad(csalad):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad,alcsalad):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad)
        self.alcsalad=alcsalad

class nemzetiseg(alcsalad):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad,alcsalad,nemzetiseg):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad,alcsalad)
        self.nemzetiseg=nemzetiseg

class nemek(nemzetiseg):
    def __init__(self,orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad,alcsalad,nemzetiseg,nemek):
        super().__init__(orszag,torzs,altorzs,foosztaly,osztaly,alosztaly,alosztalyag,oregrend,rend,alrend,csalad,alcsalad,nemzetiseg)
        self.nemek=nemek
