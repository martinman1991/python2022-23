import random

evek=[random.randint(2004, 2008) for i in range(10)]
honapok=[random.randint(1, 12) for i in range(10)]
napok=[random.randint(1, 31) for i in range(10)]

datumok=[[evek[i],honapok[i],napok[i]] for i in range(10)]

for datum in datumok:
    print(datum[0], datum[1], datum[2])