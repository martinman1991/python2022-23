import random

evek=[random.randint(2004, 2008) for i in range(100000)]
honapok=[random.randint(1, 12) for i in range(100000)]
napok=[random.randint(1, 31) for i in range(100000)]

datumok=[[evek[i],honapok[i],napok[i]] for i in range(100000)]

for datum in datumok:
    print(datum[0], datum[1], datum[2])
