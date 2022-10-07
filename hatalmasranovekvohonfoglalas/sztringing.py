nev = input("Aggy név pls: ")
print("A " + nev + " nevet írtad be.")

print("A {belsonev} nevet írtad be.".format(belsonev=nev))

if len(nev)<5:
    print("Your {belsonev} penis is very tiny.".format(belsonev=nev))
elif len(nev)>=10:
    print("Úristen very big {belsonev} penis.".format(belsonev=nev))
be="nemvegjel"
szavak=[]
while be!="":
    be=input("Type befele something: ")
    szavak.append(be)

#szavak.remove("")
#szavak.pop(-1)
#szavak.pop(len(szavek)-1)
szavak=szavak[:-1]

print(szavak)
