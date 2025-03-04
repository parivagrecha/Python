#Button 
from tkinter import *
root = Tk()
root.geometry("700x600")
def name():
    print("My name is pari")
def id():
    print("My id is 23AI020")
def sport():
    print("My favourite sport is chess")
def hello():
    print("Hello Tkinter thanks for information")
frame = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
frame.pack(side=LEFT,anchor="nw")
b1=Button(frame,fg="red", text="Enter your name", command=name)
b1.pack(side = LEFT)
b2=Button(frame,fg="red", text="Enter your college I'D", command=id)
b2.pack(side = LEFT)
b3=Button(frame,fg="red", text="Enter your favourite sports", command=sport)
b3.pack(side = LEFT)
b4=Button(frame,fg="red", text="Print now", command=hello)
b4.pack(side = LEFT)


root.mainloop()