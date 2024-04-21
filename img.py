

# Import Module
from tkinter import *
import dec, enc

root = Tk()
root.geometry('350x200')
 


def eclicked():
    enc.Encrypt(root)

    

def dclicked():
    dec.Decrpyt(root)
    


encrypt = Button(root, text = "Encrypt" , command=eclicked)

decrypt = Button(root, text = "Decrypt" , command=dclicked)


encrypt.grid(column=1, row=7, ipadx= 5, padx = 5)
decrypt.grid(column=2, row=7, ipadx= 5, padx = 5)


root.mainloop()