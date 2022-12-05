def oszlopba(munkalista,db):
    for i in range(len(munkalista)):
        print(munkalista[i],end=" ")
        if i%db==db-1:
            print()

lista=[]

for i in range(10):
    lista.append(int(input("Kérek egy számot: ")))
print(lista)

lista=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(lista)):
    print(lista[i],end=" ")
    if i%3==2:
        print()
        
print()
szamKeres=int(input("Kérek egy számot: "))
if szamKeres in lista:
    print("Van benne")
else:
    print("Nincs benen")

oszlopba(lista,5)
