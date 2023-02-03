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
   print(sorsolt[2]+"pont")
else:
   print("0 pont")
   print("a helyes válasz: " + str(sorsolt)[1])
