# -*- coding: utf-8 -*-
from accountLogin import acc
from tkinter import *
#from tkinter.ttk import *


window = Tk()

window.title("Welcome to Cancer Prediction")
window.geometry('500x500')
window.configure(background='brown')
window.minsize(width=550,height=400)
window.maxsize(width=550,height=400)
colour = StringVar()
colour.set('black')
def colourUpdate():
    colour.set('red')
    root.update()


# window.overrideredirect(True)
# window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
lb1 = Label(window, text="WELCOME",anchor=CENTER,fg = colour.get(),bg="brown", font=("Arial Bold",50))
lb2 = Label(window, text="TO",anchor=CENTER,fg = colour.get(),bg="brown", font=("Arial Bold", 50))
lb3 = Label(window, text="CANCER",anchor=CENTER,fg = colour.get(),bg="brown", font=("Arial Bold", 50))
lb4 = Label(window, text="PREDICTION",anchor=CENTER,fg = colour.get(),bg="brown", font=("Arial Bold", 50))

lb1.grid(row=1, column=3)
lb2.grid(row=2, column=3)
lb3.grid(row=3, column=3)
lb4.grid(row=4, column=3)

submit = Button(window, text="NEXT", fg="Black",
                 bg="Red",command=acc)
submit.grid(row=16, column=3)


window.mainloop()