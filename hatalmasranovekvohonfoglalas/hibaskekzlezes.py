lista=["Bence","László","Ferenc"]
lista.append("Martin")

try:
    print(lista[3])
except:
    print("Probléma van báttya")
else:
    print("Műkszik gechi")
finally:
    print("Alsó szöveg")

szam=""
while szam=="":
    try:
        szam=int(input("Number pls: "))
    except ValueError:
        print("Hallod tes számot kéne beirkálnod nem mást.")
    except IndexError:
        print("Tesomsz valamit rosszul csinálszs")

print(szam)
