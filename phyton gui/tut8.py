#frame 
from tkinter import*
root = Tk()
root.geometry("700x600")
f1= Frame(root , bg="grey", borderwidth=6,relief=SUNKEN)
f1.pack(side = LEFT, fill="y")
f2 = Frame(root, borderwidth=8,bg="grey",relief=SUNKEN)
f2.pack(side = TOP,fill="x")
l = Label(f1,text="Project Tkinter - Pycharm")
l.pack(pady=142)
l = Label(f2,text="Welcom To Mystic Teller", font="Helvetica 16 bold", fg="red",pady=22)
l.pack()
root = mainloop()