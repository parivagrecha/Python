from tkinter import *
root = Tk()
root.geometry("700x500")
root.title("My GUI with Harry")

#Important Label option 
#text - add the text 
#bd - background
#fg - foreground
#font - set the font 
#1font type = ("comicsansms", 19, "bold")
#2font type = "comicsansms 19 bold"  
#padx - x padding
#pady - y padding
#relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
title_label = Label(text = ''' 
Abdul Rashid Salim Salman Khan (pronounced [səlˈmɑːn xɑːn]; born 27 December 1965)[3] is an Indian actor, film
producer,\n and television personality who predominantly works in Hindi films. In a career spanning over 
three decades, Khan has\n received numerous awards, including two National Film Awards as a film producer,
and two Filmfare Awards as an actor.[4]\n He is cited in the media as one of the most commercially successful
actors of Indian cinema.[5][6] Forbes has included \n Khan in listings of the highest-paid celebrities in the world,
in 2015 and 2018, with him being the highest-ranked Indian \n in the latter year.[7][8][9][10] Khan has starred 
in the annual highest-grossing Hindi film of 10 individual years, the \n highest for any actor''', bg = "grey" 
, fg = "purple", padx=35, pady=98, font="comicsansms 19 bold" , borderwidth=3, relief= GROOVE)

# Important Pack Options
# anchor = nw,ew,ws,es,ns
#side = top, bottom, right, left
#by default top 
#fill = fill= x(x me felta jayega) fill = y(y me felta jayega )
#padx = 
#pady = 

title_label.pack(side = BOTTOM, anchor ="nw", fill =X)





root.mainloop()