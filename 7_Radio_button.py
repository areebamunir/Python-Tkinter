# Radio Button Implementation

from tkinter import *
root=Tk()
root.title("Radio button")
root.geometry("800x500+200+80")
#root.config(bg="#262626")
root.resizable(False,False)

gender=Label(root,text="SELECT GENDER: ",font=("times new roman",20,"bold"),fg="black").place(x=100,y=50)

def gender_func():
    print(gender.get())

# variable declaration
gender=StringVar()

male=Radiobutton(root,text="MALE",value="male",variable=gender,font=("times new roman",18,"bold"),fg="black").place(x=100,y=150)
female=Radiobutton(root,text="FEMALE",value="female",variable=gender,font=("times new roman",18,"bold"),fg="black").place(x=250,y=150)
gender.set("male")
btn=Button(root,text="SHOW",font=("times new roman",25,"bold"),command=gender_func,bg="lightgrey").place(x=260,y=200,width=150,height=50)

root.mainloop()