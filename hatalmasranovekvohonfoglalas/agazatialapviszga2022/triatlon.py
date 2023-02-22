def ido2mp():
    pass

eredmenyek=[]

f=open("triatlon.txt")
for egySor in f:
    temp=egySor.replace("\n","").split(";")
    eredmenyek.append(temp)

f.close()

eredmenyek.pop(0)

#2. feladat
print("2. Feladat")
print("A versenyen {} versenyző indul.".format(len(eredmenyek)))

#3. feladat
print("3. feladat")

