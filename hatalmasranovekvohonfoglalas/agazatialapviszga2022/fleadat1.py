print("1. feladat")
szoveg=input("Kérek egy szöveget: ")

szam=" "

while type(szam)!=int:
    try:
        szam=int(input("Kérek egy egész számot: "))
    except:
        print("Ez nem egész szám!")

try:
    print(szoveg[szam]*szam)
except:
    print("Sajnos nincs ilyen betű.")
