# Form scroll bar

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Scroll bar")
root.geometry("800x500+250+50")
root.config(bg="#262626")

frame1=Frame(root,bd=2,relief=RIDGE)
frame1.place(x=250,y=50,height=300,width=200)

scrolly=Scrollbar(frame1,orient=VERTICAL)
scrolly.pack(side=RIGHT,fill=Y)

data=Listbox(frame1,font=("ariel",20),justify=CENTER,yscrollcommand=scrolly.set)
data.pack()
scrolly.config(command=data.yview)
for i in range(0,101):
    data.insert(i,"DATA: "+str(i))

root.mainloop()