import random
import math


#l=[]
#for i in range(10):
#    szam=random.random()
#    l.append(math.floor(szam*90)+10)
#print(l)

#l=[]
#for i in range(10):
#    l.append(random.randint(10,99))
#print(l)

#print(random.randint(-1000,1000)*3)
#l=[]
#for i in range(10000):
#    l.append(random.randint(-1000,1000)*3)
#print(l)
#print(sum(l))

#l5=[]
#for e in l:
  #  if e%5==0:
   #  l5.append(l)
#print(l5)

#print(random.randrange(167,1667,2)*6)

#print((random.randint(83,832)*2+1)*6)

szavak=["alma","körte","barack","banán","dinnye","szőlő"]

#random.seed(1)
print(szavak[random.randint(0,len(szavak)-1)])

print(random.choice(szavak))

nagyLista=[]
for e in szavak:
    #print(e)
    kisLista=[]
    kisLista.append(e)
    kisLista.append(random.randint(12,312))
    #print(kisLista)
    nagyLista.append(kisLista)

print(nagyLista)


for e in nagyLista:
    print(e[0].ljust(10),str(e[1]).rjust(4),"kg")
