from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Python GUI")
root.geometry("800x500+200+80")
root.config(bg="#262626")
def message():
    messagebox.showerror("ShowError","This is Show Error MessageBox")

def message2():
    messagebox.showinfo("ShowInfo","This is Show Info MessageBox")

def message3():
    messagebox.showwarning("ShowWarning","This is Show Warning MessageBox")

btn1=Button(root,text="message1",command=message).place(x=50,y=50,width=100,height=40)
btn2=Button(root,text="message2",command=message2).place(x=160,y=50,width=100,height=40)
btn3=Button(root,text="message3",command=message3).place(x=270,y=50,width=100,height=40)

root.mainloop()