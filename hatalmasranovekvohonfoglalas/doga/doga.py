#1. feladat
adatok=[]
f=open("utca.txt","r")
for sor in f:
    temp=sor.replace("\n","").split(";")
    adatok.append(temp)

f.close()
adatok.pop(0)
#2. feladat

print("A mintában {} telek szerepel".format(len(adatok)))

#3. feladat
adoszam=int(input("Egy tulajdonos adószáma: "))
for adoszam in adatok:
    print(adoszam[0])
