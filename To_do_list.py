import tkinter as tk
from tkinter import messagebox

class to_dolist:
    def __init__(self,root):
        self.root=root
        self.root.title("To_Do_List")
        
        self.tasks=[]

        self.label1=tk.Label(root,text="To Do List App",font="ariel,25,bold",width=35,bg="yellow",fg="black")
        self.label1.grid(columnspan=2)
        
        self.label2=tk.Label(root,text="Enter your task here:",font="ariel,15,bold",width=17,bg="skyblue",fg="black")
        self.label2.grid(row=1,column=0,pady=10,padx=10,sticky="w")

        self.task_entry=tk.Entry(root,width=30)
        self.task_entry.grid(row=2,column=0,padx=10)
        self.task_entry.config(font=("Arial", 15))

        self.addtask=tk.Button(root,text="Addtask",fg="white",bg="green",command=self.add_task)
        self.addtask.grid(row=2,column=1,padx=10)

        self.label3=tk.Label(root,text="Tasks:",font="ariel,15,bold",width=8,bg="skyblue",fg="black")
        self.label3.grid(row=3,columnspan=2,pady=10)

        self.task_listbox=tk.Listbox(root,width=35,height=10,font="Arial, 15")
        self.task_listbox.grid(row=4,columnspan=2)
    

        self.removetask=tk.Button(root,text="Removetask",borderwidth=3,font="bold 9",fg="white",bg="red",relief="raised",command=self.remove_task)
        self.removetask.grid(row=5,columnspan=2,pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_task = self.task_listbox.get(selected_index)
            self.tasks.remove(selected_task)
            self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()


if __name__ == "__main__":
    root=tk.Tk()
    obj=to_dolist(root)
    tk.mainloop()