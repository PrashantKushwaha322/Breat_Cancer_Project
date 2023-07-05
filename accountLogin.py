# -*- coding: utf-8 -*-
from tkinter import *
from PIL import ImageTk
from oldUserLogin import old
from newUserLogin import newUser
def acc():
    main_screen = Tk()# create a GUI window
    main_screen.configure(background='khaki')
    main_screen.geometry("500x500")  # set the configuration of GUI window
    main_screen.minsize(width=550,height=400)
    main_screen.maxsize(width=550,height=400)
    main_screen.title("Account Login")  # set the title of GUI window
    #ogo = tkinter.PhotoImage(file="cancercell.gif")



    #w = Label(main,compound=tkinter.CENTER,image=logo).pack()
    
        
        
    Button(main_screen, text='OLD USER',width=30,height=7,bg='white',command=old,fg='black').place(x=160,y=15)
    Button(main_screen, text='NEW USER',width=30,height=7,bg='white',command=newUser,fg='black').place(x=160,y=160)
    main_screen.mainloop()  
