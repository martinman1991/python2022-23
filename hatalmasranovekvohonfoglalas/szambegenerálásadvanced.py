import random

minimErtek=int(input("Aadd meg hol kezdődjőn: "))
maximErtek=int(input("ADd meg hol végetződjön: "))
mennyiErtek=int(input("Add meg hogy meniy szam leygen bene: "))

lista=[]

for i in range(mennyiErtek):
    lista.append(random.randint(minimErtek,maximErtek))

print(lista)

legnagyobb=max(lista)
egyseg=80//legnagyobb

for e in lista:
    print("*"*(e*egyseg))

#3 jegyű számbekérés

szam=[]
while len(szam) !=3:
    szam=input("Kéekrkelk egy háoerm jegjű szaamt: ")

szam=int(szam)

if szam%12==0:
    print("osz6ó")
print(szam)
