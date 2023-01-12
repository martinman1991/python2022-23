f=open("proba.txt","w")
f.write("helo")
f.write("\n")
f.write("vörld")

f.close()

f=open("proba.txt","r")

szoveg=f.read()

sorok=szoveg.split("\n")
print(sorok)
print(szoveg)

f.close()

f=open("proba.txt","r")
sorok=[]

for sor in f:
    sorok.append(sor.replace("\n",""))
    
print(sorok)
f.close()
