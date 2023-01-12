import random

szam=[]
for i in range(8):
    szam.append(int(input("Kérek nyolc darabszámot: ")))
print(szam)
print()

oszlopszam=szam
for i in range(len(oszlopszam)):
    print(oszlopszam[i],end="")
    if i%4==2:
        print()
print()

negyesfeladat=sum(szam)
print()
print(negyesfeladat)
print()

betu=input("Kérek egy betűt: ")
szoveg="Nulla quis mi augue. Nunc vel pretium lectus. Aenean laoreet ornare ornare. Ut vitae elit et sapien fringilla iaculis ac at felis. Aenean scelerisque, diam non pellentesque rhoncus, risus lorem porttitor leo, ac consectetur nisi massa vitae sem. Nulla tempus diam id bibendum lobortis. Vestibulum porta neque id risus cursus, eget sodales nunc fermentum. Nulla facilisi. Suspendisse egestas orci a luctus fringilla. Cras dapibus ipsum nisl, non dapibus ex fermentum vitae."
print(szoveg)
szovegszamlalas=szoveg.count(betu)
print(szovegszamlalas)
print()

szoveg2=szoveg[::-1]
print(szoveg2)
print()

szoveg3=szoveg.replace("orna","")
print(szoveg3)
print()
