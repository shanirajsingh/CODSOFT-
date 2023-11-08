import tkinter as tk
import math as mt
import tkinter.messagebox
from tkinter.constants import SUNKEN

class calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x400")

        self.frame = tk.Frame(self.root,bg="grey")
        self.frame.pack()

        self.entry = tk.Entry(self.frame, relief=SUNKEN,font="bold", borderwidth=3, width=20)
        self.entry.grid(row=0, column=0,columnspan=5, ipady=2, pady=10)
        self.entry.config(font=("Arial", 20))

        clear_button=tk.Button(self.frame,text="Clear",font="8",bg="red",fg="black",width=5,pady=5,command=self.clear)
        clear_button.grid(row=1,column=0,padx=10,pady=5)

        self.AC_button=tk.Button(self.frame,text="AC",font="15,bold",bg="orange",fg="black",width=5,pady=5,command=self.delete)
        self.AC_button.grid(row=1,column=1,padx=10,pady=5)
        
        self.squrt_button=tk.Button(self.frame,text="√",font="15,bold",bg="gold1",fg="black",width=5,pady=5,command=lambda:self.operation("√"))
        self.squrt_button.grid(row=1,column=2,padx=10,pady=5)
        
        self.divide_button=tk.Button(self.frame,text="/",font="15",bg="gold1",fg="black",width=5,pady=5,command=lambda:self.operation("/"))
        self.divide_button.grid(row=1,column=3,padx=10,pady=5)
        
        self.multiply_button=tk.Button(self.frame,text="x",font="15",bg="gold1",fg="black",width=5,pady=5,command=lambda:self.operation("*"))
        self.multiply_button.grid(row=2,column=3,padx=10,pady=5)
        
        self.Substract_button=tk.Button(self.frame,text="-",font="15",bg="gold1",fg="black",width=5,pady=5,command=lambda:self.operation("-"))
        self.Substract_button.grid(row=3,column=3,padx=10,pady=5)
        
        self.addition_button=tk.Button(self.frame,text="+",font="15",bg="gold1",fg="black",width=5,pady=5,command=lambda:self.operation("+"))
        self.addition_button.grid(row=4,column=3,padx=10,pady=5)
        
        self.button12=tk.Button(self.frame,text="=",font="15",bg="green",fg="black",width=5,pady=5,command=self.equal)
        self.button12.grid(row=5,column=3,padx=10,pady=5)
        
        self.button1=tk.Button(self.frame,text="9",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(9))
        self.button1.grid(row=2,column=0,padx=10,pady=5)
        
        self.button2=tk.Button(self.frame,text="8",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(8))
        self.button2.grid(row=2,column=1,padx=10,pady=5)
        
        self.button3=tk.Button(self.frame,text="7",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(7))
        self.button3.grid(row=2,column=2,padx=10,pady=5)
        
        self.button4=tk.Button(self.frame,text="6",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(6))
        self.button4.grid(row=3,column=0,padx=10,pady=5)
        
        self.button5=tk.Button(self.frame,text="5",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(5))
        self.button5.grid(row=3,column=1,padx=10,pady=5)
        
        self.button6=tk.Button(self.frame,text="4",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(4))
        self.button6.grid(row=3,column=2,padx=10,pady=5)
        
        self.button7=tk.Button(self.frame,text="3",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(3))
        self.button7.grid(row=4,column=0,padx=10,pady=5)
        
        self.button8=tk.Button(self.frame,text="2",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(2))
        self.button8.grid(row=4,column=1,padx=10,pady=5)
        
        self.button9=tk.Button(self.frame,text="1",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(1))
        self.button9.grid(row=4,column=2,padx=10,pady=5)
        
        self.button10=tk.Button(self.frame,text=".",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation("."))
        self.button10.grid(row=5,column=0,padx=10,pady=5)
        
        self.button11=tk.Button(self.frame,text="0",font="15",bg="black",fg="white",width=5,pady=5,command=lambda:self.operation(0))
        self.button11.grid(row=5,column=1,padx=10,pady=5)
        
        self.factorial_button=tk.Button(self.frame,text="x!",font="15,bold",bg="gold1",fg="black",width=5,pady=5,command=lambda:self.operation("!"))
        self.factorial_button.grid(row=5,column=2,padx=10,pady=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def operation(self,click):
        self.entry.insert(tk.END, click)
    
    def squrt(self):
        self.current_text = self.entry.get()
        self.new_text = int(self.current_text[1:])
        self.new_text = mt.sqrt(self.new_text)
        self.entry.delete(0, tk.END)  
        self.entry.insert(0, self.new_text) 
    
    def factorial(self):
        self.current_text = self.entry.get()
        self.new_text = int(self.current_text[:-1])
        self.new_text = mt.factorial(self.new_text)
        self.entry.delete(0, tk.END)  
        self.entry.insert(0, self.new_text)  
    
    
    def equal(self):
        try: 
            if "√" in self.entry.get():
                self.squrt()
            elif "!" in self.entry.get():
                self.factorial()
            else:    
                y = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, y)
        except:
            tkinter.messagebox.showinfo("Error", "Syntax Error")
    
    
    def clear(self):
        self.entry.delete(0, tk.END)
    
    def delete(self):
        self.current_text = self.entry.get()
        self.new_text = self.current_text[:-1]  
        self.entry.delete(0, tk.END)  
        self.entry.insert(0, self.new_text) 

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy() 

if __name__ == "__main__":
    root=tk.Tk()
    obj=calculator(root)
    tk.mainloop()
 
