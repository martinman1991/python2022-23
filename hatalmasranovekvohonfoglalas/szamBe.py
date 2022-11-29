#számbakérő modul
#Többféel paraméterezéssel
#2022.11.18 Balatincz Martin

def szamBe(szoveg,tort=False,minimum=False,maximum=False):
#    print(szoveg)
#    print(tort)
#    print(minimum)
    hiba=True
    while hiba:
        try:
            if tort:
                szam=float(input(szoveg))
            else:
                szam=int(input(szoveg))
        except:
            print("valami nem jo gec")
        else:
            hiba=False
szamBe("Adgyá meg numbert ppölös: ",tort=True,minimum=10)
