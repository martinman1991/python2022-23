import random

f=open("felszam.txt","r")

kerdesek=[]
for sor in f:
   josor=sor.replace("\n","")
   josor2=f.readline().replace("\n","")
   temp=josor2.split(" ")

   kerdesek.append([josor, int(temp[0]), int(temp[1]), temp[2]])

f.close()

print("2. Feladat")
print("Az adatfájlban " + str(len(kerdesek)) + "jkérdés van")

matek=[]
for e in kerdesek:
   if e[3]=="matematika":
      matek.append(e[2])

valaszok=[]
for e in kerdesek:
   valaszok.append(e[1])

valaszok=[e[1] for e in kerdesek]
print("A válaszok értéke {}-től {}-ig tart".format(min(valaszok),max(valaszok)))

temakorok=[]
for e in kerdesek:
   if e[3] not in temakorok:
      temakorok.append(e[3])

print("5. feladat")
print("A témakörök: "+ ", ".join(temakorok))


print("6. feladat")
beker=input("Milyen témakörből szeretne kérdést kapni? ")
ujLista=[e for e in kerdesek if e[3]==beker]

sorsolt=random.choice(ujLista)

valasz=input(sorsolt[0])
if int(valasz)==sorsolt[1]:
   print(sorsolt[2]+" pont")
else:
   print("0 pont")
   print("a helyes válasz: "+ str(sorsolt)[1])

print("7, fekadat")

lista10=[]
for i in range(10):
   r=random.choice(kerdesek)
   while r in lista10:
      r.random.choice(kerdesek)

   lista10.append(r)

print(lista10)

random.shuffle(kerdesek)
lista10=kerdesek[0:10]

print(len(lista10))

f.open("tesztfel.txt","w")
ossz=0

for e in lista10:
   f.write(str(e[2])+" "+str(e[1])" "+str(e[0])+"\n")
   ossz+=e[2]

f.write("A feladatsorra összesen {0} pont adható.".format(ossz))
f.close()

