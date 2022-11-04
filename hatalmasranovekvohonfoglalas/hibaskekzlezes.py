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

try:
    szam=int(input("Number pls: "))
except:
    pass

print(szam)
