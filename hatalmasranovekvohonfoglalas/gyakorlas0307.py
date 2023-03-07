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
