from tkinter import *
root=Tk()
root.title("Python GUI")
root.geometry("800x500+200+80")
#root.config(bg="#262626")
root.resizable(False,False)

def get_data():
    print(check_var.get())

#check_var=IntVar()            -----for int type of variable
check_var=StringVar()
check_=Checkbutton(root,text="ACCEPT?NOT",onvalue="on",offvalue="off",variable=check_var,font=("ariel",25,"bold")).place(x=260,y=150)
check_var.set("off")         #for default seeting of checked button
btn=Button(root,text="SHOW",font=("times new roman",25,"bold"),bg="lightgrey",command=get_data).place(x=260,y=200,width=150,height=50)

root.mainloop()