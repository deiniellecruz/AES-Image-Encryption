

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Crypto.Cipher import AES
from PIL import ImageTk, Image
import hashlib
import os


def Decrpyt(master):
    root = Toplevel(master)
    
    def decrypt():
    
        key = key_entry.get()


        if key == "":
            messagebox.showinfo("Key Notice","Please enter a Key.")

        else:
            #get img file
            filename = filedialog.askopenfilename()

            if filename is not None:
                file_path = os.path.dirname(filename)
                file_relpath=os.path.relpath(filename)
                #print(filename)
                #print(file_path)

                #generate initilization vector
                x=hashlib.sha256(key.encode()) 
                hashdigest = x.digest()
                key = hashdigest
                iv_array = hashdigest.ljust(16)[:16]
                #print("Encoding key is: ",key)

                #read the img data or the plaintext from file
                file = open(filename,'rb')
                img_data = file.read()
                #print(img_data)

                file.close()

                #decryption on plaintext using AES
                decipher = AES.new(key, AES.MODE_CFB, iv_array)
                plaintext = decipher.decrypt(img_data)

                #write cipher text on the file
                enc_file = open(file_path +"/"+file_relpath, "wb")
                enc_file.write(plaintext)
                enc_file.close()    
                messagebox.showinfo("Notice",
                            "decrypted successfully. File is: "+file_relpath)

    

    #GUI
    root.geometry('426x240')
    frame = Frame(root)
    frame.pack(padx= 50, pady= 10)
    decrypt_btn = Button(frame, text = "Decrypt", command= decrypt)
    title = Label(frame, text= "Image Decryption")
    title.config(font=('arial',20,'bold'))
    key_label = Label(frame, text="Enter Key for Decryption:" )
    key_entry = Entry(frame, width= 30, show='$')
    title.grid(row= 0 , column= 1 , columnspan= 2, pady=5)
    key_label.grid(row=1, column=1, sticky='e' , )
    key_entry.grid(row=1, column=2, sticky='w',pady = 10)
    decrypt_btn.grid(row=3, column=2,sticky='w', ipadx = 3, ipady = 3, pady= 4)
    root.grab_set()
