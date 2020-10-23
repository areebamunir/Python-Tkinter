# Teaxtarea in a GUI window

from tkinter import *
root=Tk()
root.title("Textarea")
root.geometry("800x500+200+80")
root.config(bg="#262626")
root.resizable(False,False)

# function to get input and return output
def show_data():
    #provide index in floating number does not use variable in text
    #print(Text_field.get('1.0',END))
    var_data.set(str(Text_field.get('1.0',END)))
    print(var_data.get())

# string type variable declaration
var_data=StringVar()

# textbox
Text_field=Text(root)
Text_field.place(x=50,y=80,width=400,height=150)

# button
btn_get=Button(root,text="SHOW",font=("times new roman",25,"bold"),bg="gray",fg="white",activebackground="gray",activeforeground="white",cursor="hand2",command=show_data).place(x=100,y=300,width=150,height=40)

root.mainloop()