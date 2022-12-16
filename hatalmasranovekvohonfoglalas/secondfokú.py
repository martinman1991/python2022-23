import math

#a*x2+b*x+c

a = int(input("a="))

b = int(input("b="))

c = int(input("c="))

#(-b+-gyök(b2-4*a*c)/2a

diszkriminans=b*b-4*a*c
if diszkriminans<0:
    print("hülye fasz vagy")
elif diszkriminans==0:
    megoldas=-b /2*a
    print("hallod te kalányoshermész a megoldás: {}".format(megoldas))

#gyok=math.sqrt(1)
#print(gyok)

