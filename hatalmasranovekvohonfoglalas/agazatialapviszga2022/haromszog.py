def haromszog:

    vissza=[]
    for i in range(3):
        while type(szam)!=int:
            try:
                szam=int(input("Kérek egy három egész számot: "))
            except:
                print("Ez nem egész szám!")
        vissza.append(szam)
    return vissza
