def oszlopVissza(hanyadik):
    oszlop=[]
    for e in tabla:
        oszlop.append(e[hanyadik-1])
    return oszlop

def oszlopVissza2(hannyalOszthato):
    return [e[hannyalOszthato-1::hannyalOszthato] for e in tabla]

def t(hanyadik):
    oszlop=[e[5::6] for e in tabla]
    return oszlop

gyumolcsok=["alma","szőló","körte","barac","dragonfruit","licsi"]
print("Ennyi gyümölcs van: {0}".format(len(gyumolcsok)))
#gyumolcsok[3]="barack"
#gyumolcsok[3]+="k"
print(gyumolcsok.index("barac"))
index=gyumolcsok.index("barac")
gyumolcsok[index]+="k"
#gyumolcsok[gyumolcsok.index("barac")]+="k"
print(gyumolcsok[3])

print("Rövid gyümölcsok")
rovid=[]
for i in range(len(gyumolcsok)):
    if len(gyumolcsok[i])<=4:
        rovid.append(gyumolcsok[i])
print(rovid)

rovid=[]
for e in gyumolcsok:
    if len(e)<=4:
        rovid.append(e)
print(rovid)

rovid=[e for e in gyumolcsok if len(e)<5]
print(rovid)

rovid=[]
i=0
while i<len(gyumolcsok):
    if len(gyumolcsok[i])<5:
           rovid.append(gyumolcsok[i])
    i+=1
print(rovid)

rovid=[]
i=0
while True:
    print(i)
    if len(gyumolcsok[i])<5:
        rovid.append(gyumolcsok[i])
    if len(gyumolcsok)-1==i:
        break
    i+=1

print(gyumolcsok[-2:])
print(gyumolcsok[:2])
print(gyumolcsok[len(gyumolcsok)-2:])
print(gyumolcsok[1:-1])
print(gyumolcsok[1:5])

paratlan=gyumolcsok[1::2]
print(paratlan)
paros=gyumolcsok[0::2]
print(paros)

forditott=gyumolcsok
forditott.reverse()
print(", ".join(forditott))

print(", ".join(forditott[::-1]))

tabla=[]
for i in range(20):
    sor=[]
    for k in range(10):
        sor.append((i+1)*(k+1))
    tabla.append(sor)

print(tabla)

oszlop=[]
for e in tabla:
    oszlop.append(e[0])

print(oszlop)
print(oszlopVissza(5))
print(oszlopVissza(6))

oszlop=[e[:3] for e in tabla]
oszlop=[e[4:7] for e in tabla]
oszlop=[e[1::2] for e in tabla]
oszlop=[e[3::2] for e in tabla]
print(oszlop)

#print(oszlopVissza2(int(input("Szám: "))))

oszlop=[[e[2], e[7]] for e in tabla]

print(oszlop)
