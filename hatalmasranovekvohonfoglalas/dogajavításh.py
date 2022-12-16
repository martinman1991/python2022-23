szamok=[]
for i in range(10):
    szamok.append(int(input(str(i+1)+". szám: ")))
for i in szamok:
    print(str(i),end="")
print()
print("vége")

for i in range(10):
    print(str(szamok[i])+"\t",end="")
    if i%3==2:
        print()

print()
atlag=sum(szamok)/len(szamok)
print(atlag)


osszeg=0
for i in szamok:
    osszeg+=i
atlag=osszeg/len(szamok)
print(atlag)
szoveg="Integer eget pharetra magna. Nulla ex urna, congue ac tincidunt ut, interdum et metus. Phasellus nunc nunc, consectetur eu odio vitae, ullamcorper sagittis nisi. Ut quam tortor, tempus sit amet diam nec, auctor iaculis leo. Donec ut libero velit. Maecenas nisi magna, congue ut tortor quis, maximus maximus arcu. Mauris et commodo nibh. Fusce id est vehicula, consectetur mi et, molestie sapien."
betu="qwe"
while betu!="":
    betu=input("Kérek egy betűt: ")
    szoveg=szoveg.replace(betu,betu.upper())
    print(szoveg)

lista=szoveg.split(" ")
lista.reverse()
szoveg2=" ".join(lista)
print(szoveg2)
jelek=",.!?-:';"

for i in range(len(jelek)):
    szoveg=szoveg.replace(jelek[i],"")
print(szoveg)

szoveg="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam aliquet, nisl vel feugiat auctor, est nisl semper dolor, non mattis sapien ipsum eu odio. Donec fringilla lectus sed ligula sodales, vitae porttitor leo bibendum. Donec quis ligula lectus. Maecenas et ex sem. Maecenas consequat convallis lacus, quis ultricies eros dignissim sit amet. Donec ultricies est eget lacus rutrum tincidunt. Donec posuere ipsum est, vel posuere dolor consequat id. Vivamus odio ex, pharetra sit amet fringilla at, scelerisque at ex. Quisque venenatis nunc quis ex feugiat, et sodales nisl tempor. Praesent nec orci molestie, imperdiet nunc quis, rutrum sapien. Proin sodales."
