import random

def szoBeker():
    szo=input("Kérek egy szót: ")
    if szo=="":
        jelentes=""
    else:
        jelentes=input(szo+ " jelentése: ")

    return [szo,jelentes]

szavak=[]
def sokBeker():
    szo=szoBeker()
    while szo[0]!="":
        szavak.append(szo)
        szo=szoBeker()
    return szavak
    
def filebaIr(lista):
    f=open("szotar.txt","a")

    for e in lista:
        #print(e)
        f.write(" ".join(e))
        f.write("\n")
    f.close()

kerdesek=[]
def beolvas():
    f=open("szotar.txt","r")
    for sor in f:
        kerdesek.append(sor.replace("\n","").split(" "))

    f.close()
def kerdez():
    valasztott=random.choice(kerdesek)
    #print("valasztott", valasztott)
    
    rossz=[]
    for i in range(3):
        temp=random.choice(kerdesek)
      #  print("temp",temp)
        while not(temp not in rossz and temp!=valasztott):
            temp=random.choice(kerdesek)
            
            rossz.append(temp)
        #print("rosdsz",rossz)

    print("-"*40)
    print("Mit jelenet ez a szó "+ valasztott[0]+"?")

    rossz.append(valasztott)

    abc="abcdefghijklmnopqrstuvxyz"
    random.shuffle(rossz)

    i=0
    for e in rossz:
        print(abc[i]+": "+e[1])

    #szar
    valasz=input("Válassz: ")

    hol=4
    while hol>=4:
        try:
            if valasz!="":
                hol=abc.index(valasz)        
        except:
            valasz=input("Válassz újra: ")
        else:
            if hol>=4:
                valasz=input("Válassz újra: ")

  #  if valasztott[0]==rossz[hol]:
        #print("Helyes :)")
    #else:
       # print("Rossz válasz!")
    return valasztott[0]==rossz[hol][0]

def menu():
    beker=""

    while beker!="0":
        print("-"*40)
        print("Szótár program\n")
        print("1: Szavak bevitele")
        print("2: Feleltetés")
        print("0: Kilépés")
        beker=input("Válassz: ")

        if beker=="1":
            szavak=sokBeker()
            filebaIr(szavak)
        elif beker=="2":
            beolvas()
            lil_A=[]
            for i in range(10):
                    lil_A.append(kerdez())
            print("A zeredmény: {:.0%}".format(lil_A.count(True)/len(lil_A)))

menu()
#valasz bekérés
    
#beolvas()
#lil_A=[]
#for i in range (10):
  #  lil_A.append(kerdez())
#print(lil_A)

#print("A zeredmény: {:.0%}".format(lil_A.count(True)/len(lil_A)))
#szavak=sokBeker()
#filebaIr(szavak)
