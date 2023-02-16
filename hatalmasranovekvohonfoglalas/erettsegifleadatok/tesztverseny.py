def pontSzamit(valasz,helyes):
    pont=0
    for sorszam,betu in enumerate(valasz):
        if sorszam<5:
            pont+=3
        elif sorszam<10:
            pont+=4
        elif sorszam<14:
            pont+=5
        else:
            pont+=6

    return pont

f=open("valaszok.txt")

adatok=f.read().split("\n")

adatok.remove("")

f.close()

helyes=adatok[0]
adatok.remove(helyes)


valaszok=[]
for e in adatok:
    valaszok.append(e.split(" "))

#print(valaszok)

print("2. feladat: A vetélkedőn "+str(len(valaszok))+" versenyző indult. ")

versenyzo=input("3. fealadat: A versenyzp azinisítója = ")
versenyzoValasza=""


for e in valaszok:
    if e[0]==versenyzo:
       print(e[1]+"\t(a versenyző válasza)")
       versenyzoValasza=e[1]

print("{}\t(a versenyző válasza)".format([e[1] for e in valaszok if e[0]==versenyzo][0]))


print("4. feladat")
print(helyes+"\t(a helyes megoldás)")
print(valaszok[1])

for sorszam,betu in enumerate(versenyzoValasza):
    if betu==helyes[sorszam]:
        print("+",end="")
    else:
        print(" ",end="")

print("\t(a versenyző heéyes valaszai)")

feladat=int(input("5. feladat: A feladat sorszáma "))

db=0
for e in valaszok:
    if e[1][feladat]==helyes[feladat]:
        db+=1
print("A feladatra {0} fő, a versenyzők {1:.2%}-a adott helyes választ.".format(db,db/len(valaszok)))

f=open("pontok.txt","w")
eredmenyek=[]

for e in valaszok:
    pont=pontSzamit(e[1],helyes)
    f.write(e[0]+" "+str(pont)+"\n")
    eredmenyek.append([pont,e[0]])
f.close()

csakPontok=set()
for e in eredmenyek:
        csakPontok.add(e[0])

top3=list(csakPontok)[-3:]
top3.sort()
top3.reverse()

for sorszam,i in enumerate(top3):
    #print(i)
    for e in eredmenyek:
        if e[0]==1:
            print(" "(1)[1])
