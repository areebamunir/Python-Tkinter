from tkinter import *
root=Tk()
root.title("Wlcome Window")
root.geometry("550x800+300+80")
root.config(bg="#262626")
root.resizable(False,False)
def get_name():
    lbl_result.config(text=str(txt_Entry.get()))

#Labels
lbl_title=Label(root,text="WELCOME..",font=("times new roman",40,"bold"),bg="grey",fg="orange").pack(fill=X)
lbl_title2=Label(root, text="ENTER YOUR NAME",font=("verdana",26,"bold"),bg="#262626",fg="red").pack(fill=X,pady=25)

#Input entry for name
txt_Entry=Entry(root,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
txt_Entry.place(x=0,y=155,relwidth=1)

lbl_title3=Label(root,bg="yellow",bd=4,).pack(fill=X,pady=45,padx=50)

#button to enter name(text) in a window
btn_get=Button(root,text="Enter",font=("times new roman",25,"bold"),bg="brown",fg="white",activebackground="blue",activeforeground="red",cursor="hand2",command=get_name).place(x=180,y=270,width=200,height=60)

lbl_title4=Label(root,bg="yellow",bd=4,padx=50).place(x=50,y=370,width=450)

#Display input result of name
lbl_result=Label(root,font=("ariel",20,"bold"),bg="#262626",fg="green")
lbl_result.place(x=0,y=400,relwidth=1,height=80)

root.mainloop()