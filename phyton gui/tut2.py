from tkinter import *
from PIL import Image , ImageTk

parikumari_root = Tk()

# gui logic here 
# Width x Height
parikumari_root.geometry("646x459")
# Width , Height
parikumari_root.minsize(300,100)
# Width , Height 
parikumari_root.maxsize(1000,800)
Photo=PhotoImage(file = "Screenshot 2024-08-13 010352.png")
gauri_label =Label(image = Photo) 
gauri_label.pack()
gauri = Label(text="Gauri is a good girl and this is her GUI")
gauri.pack()

# for jpg image 
# image = Image.open("photo.jpg")
# photo = ImageTk.PhotoImage(image)





parikumari_root.mainloop()
