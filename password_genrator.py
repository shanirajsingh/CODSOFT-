import tkinter as tk
from tkinter import messagebox
import string
import random

class password_genrator:
    def __init__(self,root):
        self.root=root
        self.root.title("Password_Genrator")
        self.root.geometry("500x250")

        self.label1=tk.Label(self.root,text="Password Genrator",font="ariel,25,bold",width=45,bg="brown",fg="white")
        self.label1.grid(columnspan=2,pady=10)

        self.label2=tk.Label(self.root,text="Enter user name:",font=10)
        self.label2.grid(row=3)
        self.username_entry=tk.Entry(self.root,width=20)
        self.username_entry.grid(row=3,column=1,padx=10)
        self.username_entry.config(font=("Arial", 15))

        self.label3=tk.Label(self.root,text="Enter password length:",font=10)
        self.label3.grid(row=4)
        self.length_entry=tk.Entry(self.root,width=20)
        self.length_entry.grid(row=4,column=1,padx=10,pady=10)
        self.length_entry.config(font=("Arial", 15))

        self.label5=tk.Label(self.root,text="Genrated Password:",font=10)
        self.label5.grid(row=5)
        self.password_listbox=tk.Listbox(self.root,width=20,height=1,font="Arial, 15",fg="green")
        self.password_listbox.grid(row=5,column=1)
    

        self.Genrate_button=tk.Button(self.root,text="GENRATE PASSWORD",bg="blue",fg="white",command=self.genrate_password_clicked)
        self.Genrate_button.grid(row=6,column=1,pady=10)

        self.accept_task=tk.Button(self.root,text="RESET",fg="white",bg="red",command=self.reset)
        self.accept_task.grid(row=7,column=1)

    def genrate_password(self,length):
        self.characters = string.ascii_letters + string.digits + string.punctuation 
        self.password = ''.join(random.choice(self.characters) for _ in range(length))
        return self.password
   

    def genrate_password_clicked(self):
        self.username = self.username_entry.get()
        self.length = int(self.length_entry.get())
        self.password = self.genrate_password(self.length)
        self.password_listbox.insert(tk.END,self.password )
    

    def reset(self):
        self.password_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root=tk.Tk()
    obj=password_genrator(root)
    tk.mainloop()