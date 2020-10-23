# Entry and Textbox Difference

from tkinter import *
root=Tk()
root.title("Python GUI")
root.geometry("800x500+200+80")
root.config(bg="#262626")
root.resizable(False,False)
def get_name():
    # print(txt_Entry.get())
    lbl_result.config(text=str(var_txt.get()))

var_txt=StringVar()

#lbl_title=Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").pack(fill=X)
#txt_Entry=Entry(root,font=("times new roman",40,"bold"),bg="lightyellow",fg="black",bd=10,relief=GROOVE).pack(pady=10,padx=10)

#for width according to window
lbl_title=Label(root,text="Entry and Textbox Difference",font=("times new roman",30,"bold"),bg="black",fg="red").place(x=0,y=0,relwidth=1)
lbl_entry=Label(root,text="Entry: ",font=("ariel",18,"bold"),bg="#262626",fg="yellow").place(x=0,y=50)
txt_Entry=Entry(root,font=("times new roman",15,"bold"),bg="lightyellow",fg="black",textvariable=var_txt).place(x=0,y=90,width=300,height=50)

btn_get=Button(root,text="SHOW",font=("times new roman",25,"bold"),bg="gray",fg="black",activebackground="gray",activeforeground="white",cursor="hand2",command=get_name).place(x=170,y=180,width=150,height=40)

lbl_txt=Label(root,text="Textbox: ",font=("ariel",18,"bold"),bg="#262626",fg="yellow").place(x=0,y=230)
address=Text(root).place(x=50,y=270,width=400,height=180)

lbl_result=Label(root,font=("times new roman",20,"bold"),bg="#262626",fg="white")
#lbl_result.place(x=0,y=200,relwidth=1)

root.mainloop()