# ComboBox

from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Combo Box")
root.geometry("800x500+200+80")
#root.config(bg="#262626")
root.resizable(False,False)

def get_data():
    print(language.get())

#no property to change background in combobox
language=ttk.Combobox(root,values=("PHP","HTML","CSS","JavaScript","Flask"),font=("times new roman",20,"bold"),justify=CENTER,state="readonly")
language.place(x=100,y=50,width=200,height=40)
#language.current(0)         ------use to dispaly all tuple value in dropdown

language.set("Select Language")   #it set specific tuple value for initial only not in dropdown menu

btn=Button(root,text="SHOW",command=get_data).place(x=50,y=200)

root.mainloop()