from tkinter import *
import math

class forgato:
    canvas=0
    vonalak=[]
    szog=0
    szogSebesseg=0.5
    szinek=[]
    
    def __init__(self,canvas,vonalak):
        self.canvas=canvas
        self.vonalak=vonalak

        for i,betu in enumerate(self.vonalak):
            betu+=betu[:2]
            betu=self.nagyit(betu,10)
            self.vonalak[i]=self.eltol(betu,200,200)
        self.kozepSzamol()
    def rajzol(self):
        canvas.delete("all")
        vissza=[]
        self.szog+=self.szogSebesseg
        for i,betu in enumerate(self.vonalak):
            betu=self.eltol(betu,-self.kozep[0],-self.kozep[1])
            betu=self.forgat(betu,self.szog)
            betu=self.eltol(betu,self.kozep[0],self.kozep[1])
            
            self.canvas.create_line(betu, fill=self.szinek[i], width=5)
        return vissza
    
    def eltol(self,pontok,x,y):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2==1:
                vissza.append(pont+x)   
            else:
                vissza.append(pont+y)
        return vissza

    def nagyit(self,pontok,meret):
        vissza=[]
        for i,pont in enumerate(pontok):
            if i%2==1:
                vissza.append(pont*meret)
            else:
                vissza.append(pont*meret)
        return vissza
    

    def forgat(self,pontok, szog):
        vissza=[]
        for i, pont in enumerate(pontok):
            if i%2==0:
                szogRadian=math.radians(szog)
                print(len(pontok))
                x=pontok[i]*math.cos(szogRadian)-pontok[i+1]*math.sin(szogRadian)
                y=pontok[i]*math.sin(szogRadian)+pontok[i+1]*math.cos(szogRadian)
                vissza.append(x)
                vissza.append(y)
        return vissza
    def kozepSzamol(self):
        self.kozep=[0,0]
        db=0
        for betu in self.vonalak:
            xK=betu[::2]
            yK=betu[1::2]
            self.kozep[0]+=sum(xK)
            self.kozep[1]+=sum(yK)
            db+=len(xK)

        self.kozep[0]/=db
        self.kozep[1]/=db
# Create an instance of tkinter frame or window
win=Tk()

# Set the size of the tkinter window
win.geometry("1000x500")

# Create a canvas widget
canvas=Canvas(win, width=1000, height=500, bg="beige")
canvas.pack(fill = BOTH, expand = 1)

betu=[[300,30,80,30,80,300,300,300,300,150,80,150,80,30,300,30,300,300],[270,60,100,60,100,130,270,130,270,60],[270,200,100,200,100,270,270,270,270,200]]

elso=forgato(canvas,betu)
elso.szinek=["blue","blue","green","yellow","yellow","red","red"]
szog=0
while True:

    elso.rajzol()
    win.update_idletasks()
    win.update()
    #win.mainloop()
