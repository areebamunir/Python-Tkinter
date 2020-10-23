# Input Entries with button

from tkinter import *
root=Tk()
root.title("Input Entry")
root.geometry("400x500+700+80")
root.config(bg="grey")
root.resizable(False,False)

# funtion to get input and return it 
def get_name():
    # print(txt_Entry.get())
    lbl_result.config(text=str(txt_Entry.get()))

#lbl_title=Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="red").pack(fill=X)
#txt_Entry=Entry(root,font=("times new roman",40,"bold"),bg="lightyellow",fg="black",bd=10,relief=GROOVE).pack(pady=10,padx=10)

#for width according to window
lbl_title=Label(root,text="TITLE",font=("times new roman",40,"bold"),bg="white",fg="green").place(x=0,y=0,relwidth=1)
txt_Entry=Entry(root,font=("times new roman",15,"bold"),bg="lightyellow",fg="black")
txt_Entry.place(x=0,y=60,relwidth=1)

# button to display output
btn_get=Button(root,text="SHOW",font=("times new roman",25,"bold"),bg="black",fg="red",activebackground="gray",activeforeground="white",cursor="hand2",command=get_name).place(x=120,y=100,width=150,height=70)

# Label to show output result after clicking the button
lbl_result=Label(root,font=("times new roman",20,"bold"),bg="grey",fg="orange")
lbl_result.place(x=0,y=200,relwidth=1)
root.mainloop()