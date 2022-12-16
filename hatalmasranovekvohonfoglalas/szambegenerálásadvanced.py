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

szoveg="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam aliquet, nisl vel feugiat auctor, est nisl semper dolor, non mattis sapien ipsum eu odio. Donec fringilla lectus sed ligula sodales, vitae porttitor leo bibendum. Donec quis ligula lectus. Maecenas et ex sem. Maecenas consequat convallis lacus, quis ultricies eros dignissim sit amet. Donec ultricies est eget lacus rutrum tincidunt. Donec posuere ipsum est, vel posuere dolor consequat id. Vivamus odio ex, pharetra sit amet fringilla at, scelerisque at ex. Quisque venenatis nunc quis ex feugiat, et sodales nisl tempor. Praesent nec orci molestie, imperdiet nunc quis, rutrum sapien. Proin sodales."
betu="k"
print(len(szoveg.split(" ")))
szoveg2=szoveg.replace(betu,betu.upper())
print(szoveg2)
