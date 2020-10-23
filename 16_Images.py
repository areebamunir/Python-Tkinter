# Show images in png and jpg format

from tkinter import *
from PIL import ImageTk
root=Tk()
root.title("Images")
root.geometry("800x500+250+50")
#root.config(bg="#262626")

#--------- for png image---------
#icon=PhotoImage(file="Images/ninja.png")
#lbl_image=Label(root,text="  Username",padx=20,image=icon,compound=LEFT).place(x=50,y=50)

#--------- for jpg image---------
icon= ImageTk.PhotoImage(file="Images/naruto.jpg")
lbl_image=Label(root,image=icon,).place(x=0,y=0)
root.mainloop()