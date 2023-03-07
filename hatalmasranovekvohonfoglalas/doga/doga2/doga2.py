#1. feladat
jeloltek=[]
f=open("szavazatok.txt","r")
for sor in f:
    temp=sor.replace("\n","")
    jeloltek.append(temp)

#2. feladat
print("A helyhatósági választásnon {} képviselőjelölt indult.".format(len(jeloltek)))

f.close()

#3. feladat
nev=input("Képviselőnév: ")
for e in jeloltek:
    print(e)
    if nev==str(e[2]):
        print(e[1])
    else:
        print("Ilyen nevű képviselő nem szerepel a nyilvántartásban!")

#4. feladat

szavazott=[]
szavazott.append(jeloltek)

print(szavazott)
