from tkinter import *
root = Tk()
root.geometry("700x600")
# grid layout
def getvalue():
    print(f"The value of user is {uservalue.get()}")
    print(f"The value ofpassword is {passvalue.get()}")
user = Label(root,text = "username")
password = Label(root,text = "passoward")
user.grid()
password.grid(row = 1)
# variable classes in Tkinter
#BooleanVar,DoubleVar,IntVar,StringVar
uservalue = StringVar()
passvalue = StringVar()

userentry =Entry(root,textvariable = uservalue) 
passentry =Entry(root,textvariable = passvalue) 
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command=getvalue).grid()

root.mainloop()