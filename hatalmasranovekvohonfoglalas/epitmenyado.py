f=open("utca.txt")
hazak=[]

for e in f:
    hazak.append(e.replace("\n","").split(" "))

f.close()
