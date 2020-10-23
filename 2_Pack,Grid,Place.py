# How to create Labels Using Pack, Place and Grid
# Uncomment individual system section to obtain particular labels

# import tkinter as tk
from tkinter import *
root=Tk() #here root is an object
root.title("Python GUI")  #title class is use to give title to window
root.geometry("800x400+200+50")  #through geometry class we can set width and height of a window and to fix where to start window then concatenate it with +
root.resizable(width=False,height=True)  #resizable is use to restrict the mizimization of a window
root.config(bg="grey")

#----------GRID SYSTEM----------
#lbl=Label(root,text="GRID SYSTEM").grid(row=0,column=0)
#lbl=Label(root,text="GRID SYSTEM").grid(row=0,column=1)
#lbl=Label(root,text="GRID SYSTEM").grid(row=2,column=0)

#----------PACK SYSTEM----------
#lbl=Label(root,text="PACK1 SYSTEM").pack(side=LEFT)
#lbl=Label(root,text="PACK2 with fill SYSTEM").pack(expand=1,fill=BOTH)
#lbl=Label(root,text="PACK3 normal SYSTEM").pack()

#----------PLACE SYSTEM----------
#by default pack is in center
lbl=Label(root,text="PLACE SYSTEM").place(x=0,y=0)
lbl=Label(root,text="PLACE SYSTEM").place(x=400,y=300)
lbl=Label(root,text="PLACE SYSTEM").place(x=200,y=200)


root.mainloop() #mainloop help screen stay

