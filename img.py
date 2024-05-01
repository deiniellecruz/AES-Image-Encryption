

# Import Module
from tkinter import *
import dec, enc

root = Tk()
root.geometry('350x200')
 


def eclicked():
    enc.Encrypt(root)

    

def dclicked():
    dec.Decrpyt(root)
    

frame = Frame(root)
frame.pack(padx= 50, pady= 20)
encrypt = Button(frame, text = "Encrypt" , command=eclicked)

decrypt = Button(frame, text = "Decrypt" , command=dclicked)

title = Label(frame, text= "AES Encryption")
title.config(font=('arial',20,'bold'))
title.grid(row= 0 , column= 1 , columnspan= 2, pady=20)
encrypt.grid(column=1, row=1, ipadx= 5, padx = 5)
decrypt.grid(column=2, row=1, ipadx= 5, padx = 5)


root.mainloop()