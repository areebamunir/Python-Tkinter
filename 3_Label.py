# Use of Labels

from tkinter import *
root=Tk()
root.title("Python GUI")
root.geometry("400x500+700+80")
root.config(bg="grey")
root.resizable(False,False)

lbl_title2=Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="yellow",fg="red",pady=50,bd=10,relief=GROOVE).pack(fill=X,pady=20,padx=20)

lbl_title3=Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").place(x=150,y=300,height=100,width=200)

root.mainloop()