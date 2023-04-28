from tkinter import *
import math



class forgato:
    canvas=0
    vonalak=[]
    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=canvas





def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==1:
            vissza.append(pont.x)
        else:
                vissza.append(pont.y)
    return vissza

def nagyit (pontok,x,y,meret=1):
    mere=[]
    for i, pont in (pontok):
        if i%2==1:
            vissza.append(pont.x)
        else:
                vissza.append(pont.y)
        return vissza

        for i,pont in enumerate(pontok):
            if i%2==0:
                szogRadian=math.radians(szog)
                x=pontok[i]*math.cos(math.radians(szog))-pontok[i+i]*math.sin(math.radians(szog))
                y=pontok[i]*math.sin(math.radians(szog))-pontok[i+i]*math.cos(math.radians(szog))

                visza.append(x)
                visza.append(y)
        return vissza
    

win = Tk()

win.geometry("1000x200")

canvas = Canvas(win, width=500, height=500, bg="white")
canvas.pack(fill=BOTH, expand=1)

canvas.create_line(50,50,50,150,75,150,75,100,100,100,100,150,125,150,125,50,50,50, fill="red", width=5)
canvas.create_line(70,70,100,70,100,85,70,85,70,70, fill="red", width=5)
canvas.create_line(175,50,175,50,215,50,225,70,225,125,215,150,175,150,175,50, fill="red", width=5)
canvas.create_line(190,70,190,70,210,70,215,80,215,115,210,135,190,135,190,70, fill="red", width=5)
canvas.create_line(275,50,275,50,325,50,325,150,275,150,275,50, fill="red", width=5)
canvas.create_line(290,70,290,70,310,70,310,135,290,135,290,70, fill="red", width=5)
canvas.create_line(375,50,375,50,375,150,400,150,400,130,425,130,450,150,465,130,425,105,425,50,375,50, fill="red", width=5)
canvas.create_line(390,70,390,70,390,100,410,100,410,70,390,70, fill="red", width=5)
canvas.create_line(500,150,500,150,575,150,575,50,550,50,550,125,500,125,500,150, fill="red", width=5)
canvas.create_line(620,150,620,150,620,50,675,50,675,150,660,150,660,110,635,110,635,150,620,150, fill="red", width=5)
canvas.create_line(635,70,635,70,635,100,660,100,660,70,635,70, fill="red", width=5)
canvas.create_line(635,10,635,10,660,10,660,40,635,40,635,10, fill="red", width=5)
canvas.create_line(710,50,710,50,735,50,760,110,760,50,785,50,785,150,760,150,720,75,720,150,710,150,710,50, fill="red", width=5)

elso=forgat(canvas,vonalak)


for i,betu in enumerate(adorjan):
    betu+=betu[:2]
    betu=nagyit(betu,10)
    adorjan[i]=eltol(betu,200,200)

kozep=[0,0]
db=0
for betu in adorjan:
    xk=betu[::2]
    yk=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)

kozep[0]/=db
kozep[1]/=db


def rajzol(self):
    canvas.delete("all")
    szog+=0.5
    print(szog)
    for betu in adorjan:
        #innen
        betu=eltol(betu,-kozep[0],-kozep[1])
        betu=forgato(betu,90)
        betu=eltol(betu,kozep[0],kozep[1])

        canvas.create_line(betu, fill="red", width=1)

while True:
        eslo.rajzol()
        win.update_idletask()
        win.update()
    #win.mainloop()
