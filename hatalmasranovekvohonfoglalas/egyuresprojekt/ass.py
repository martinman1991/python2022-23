# Import the required libraries
from tkinter import *

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the tkinter window
win.geometry("1500x500")

# Create a canvas widget
canvas = Canvas(win, width=500, height=500, bg="white")
canvas.pack(fill=BOTH, expand=1)

# Add lines to create the letter "M"
canvas.create_line(50,50,50,150,75,150,100,50,100,150,130,150,130,50,50,50, fill="blue", width=5)
canvas.create_line(150,50,150,150,175,150,175,75,200,75,200,150,225,150,225,50,150,50, fill="blue", width=5)
canvas.create_line(250,50,250,150,275,150,275,100,300,100,300,150,338,150,338,130,320,130,320,50,250,50, fill="blue", width=5)
canvas.create_line(275,60,300,60,300,90,275,90,275,60, fill="blue", width=5)
canvas.create_line(350,60,390,60,390,90,375,90,375,150,360,150,360,90,350,90,350,60, fill="blue", width=5)
canvas.create_line(350,60,390,60,390,90,375,90,375,150,360,150,360,90,350,90,350,60, fill="blue", width=5)
canvas.create_line(400,50,420,50,420,150,400,150,400,50, fill="blue", width=5)
canvas.create_line(438,50,438,150,469,150,469,100,500,150,530,150,530,50,500,50,500,100,469,50,438,50, fill="blue", width=5)

# Run the tkinter mainloop
win.mainloop()
