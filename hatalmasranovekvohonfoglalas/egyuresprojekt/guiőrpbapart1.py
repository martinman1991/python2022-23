import math
from tkinter import *

def eltol(pontok,x,y):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            vissza.append(pont+x)   
        else:
            vissza.append(pont+y)
    return vissza

def nagyit(pontok,x,y,meret=1):
    vissza=[]
    for pont in pontok:
        vissza.append(pont*meret)
    return vissza

def forgat(pontok, szog):
    vissza=[]
    for i, pont in enumerate(pontok):
        if i%2==0:
            szogRadian=math.radians(szog)
    
            
            x=pontok[i]*math.cos(szogRadian)-pontok[i+1]*math.sin(szogRadian)
            y=pontok[i]*math.sin(szogRadian)+pontok[i+1]*math.cos(szogRadian)
            vissza.append(x)
            vissza.append(y)
        return vissza

# Import the required libraries

# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1000x500")

# Create a canvas widget
canvas=Canvas(win, width=1000, height=500, bg="beige")
canvas.pack(fill = BOTH, expand = 1)

B=[[300,30,80,30,80,300,300,300,300,150,80,150,80,30,300,30,300,300],[270,60,100,60,100,130,270,130,270,60],[270,200,100,200,100,270,270,270,270,200]]

nev=[]
for i,B in enumerate(nev):
    B+=B[:2]
    B=nagyit(B,10)
    nev[i]=eltol(B,200,200)

kozep=[0,0]
db=0
for B in nev:
    xK=betu[::2]
    yK=betu[1::2]
    kozep[0]+=sum(xK)
    kozep[1]+=sum(yK)
    db+=len(xK)

kozep[0]/=db
kozep[1]/=db

szog=0
while True:
    canvas.delete("all")
    szog+=0.5
    print(szog)
    for B in nev:
        B=eltol(B,-kozep[0],-kozep[1])
        B=forgat(B,szog)
        B=eltol(B,kozep[0],kozep[1])
        
        canvas.create_line(B, fill="green", width=5)

    #win.mainloop()
    win.update_idletasks()
    win.update()
