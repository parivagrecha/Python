from tkinter import*
from PIL import Image,ImageTk
base_root=Tk()
base_root.geometry("10000x10000")
base_root.title("Aaj tak")
base_root.minsize(300,300)

# Header for newspaper
header=Label(text= '''Pari's Newspaper''',bg = "grey" , fg = "black", padx=5, pady=8, font="comicsansms 19 bold" , 
borderwidth=3, relief= GROOVE)
header.pack(side=TOP,fill=X)

#News 1 
Photo=PhotoImage(file = "article1.png")
News1=Label(image = Photo,width=200,height=200)
News1.pack()
#News1.pack(side=TOP)
News1.pack(anchor="nw")
f1 = Label(text = '''Indian tycoon Ratan Tata has died aged 86, says the Tata Group,
the conglomerate he led for more than two decades.
Tata was one of India's most internationally recognised business leaders.
The Tata Group is one of India's largest companies, with annual revenues in excess of $100bn (£76.5bn).
In a statement announcing Tata's death, the current chairman of Tata Sons described him as a "truly uncommon leader".''',
bg = "black" , fg = "white", padx=1, pady=2, font="comicsansms 19" , borderwidth=1, relief= SUNKEN)
f1.pack(anchor="e")

#news 2 
Photo=PhotoImage(file = "article1.png")
News1=Label(image = Photo,width=200,height=200)
News1.pack()
#News1.pack(side=TOP)
News1.pack(anchor="nw")
f1 = Label(text = '''Indian tycoon Ratan Tata has died aged 86, says the Tata Group,
the conglomerate he led for more than two decades.
Tata was one of India's most internationally recognised business leaders.
The Tata Group is one of India's largest companies, with annual revenues in excess of $100bn (£76.5bn).
In a statement announcing Tata's death, the current chairman of Tata Sons described him as a "truly uncommon leader".''',
bg = "black" , fg = "white", padx=1, pady=2, font="comicsansms 19" , borderwidth=1, relief= SUNKEN)
f1.pack(anchor="e")







base_root>=mainloop()