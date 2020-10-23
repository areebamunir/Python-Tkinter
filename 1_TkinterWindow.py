# How to create window

# import tkinter as tk
from tkinter import *
root=Tk() #here root is an object
root.title("Python GUI")  #.title class is use to give title to window
root.geometry("800x400+200+50")  #through .geometry class we can set width and height of a window and to fix where to start window then concatenate it with +
root.resizable(width=False,height=True)  #.resizable is use to restrict the mizimization of a window
root.config(bg="blue")

root.mainloop()