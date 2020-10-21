from tkinter import *
root=Tk()
root.title("Python GUI")
root.geometry("800x500+300+60")
root.config(bg="whitesmoke")
root.resizable(False,False)

#function to display the input fields of form
def get_data():
    if var_check.get()==1:
        result="USERNAME: " +var_username.get()+"\nEMAIL: "+var_email.get()+"\nGENDER: "+var_gender.get()
        lbl_result.config(text=str(result))
    else:
        lbl_result.config(text="Please First Accept Terms and Conditions")
    
# varabiles
var_username=StringVar()
var_email=StringVar()
var_gender=StringVar()
var_check=IntVar()

# header label
lbl_title=Label(root,text="USER ENTRY FORM",font=("times new roman",30,"bold"),bg="black",fg="gold").place(x=0,y=0,relwidth=1)

# Username entry and label
lbl_username=Label(root,text="USERNAME",font=("ariel",19,"bold"),fg="red",bg="whitesmoke").place(x=70,y=80,height=50,width=150)
txt_username=Entry(root,textvariable=var_username,font=("times new roman",15,"bold"),bg="ivory3",fg="black").place(x=250,y=90,height=30,width=400)

# Email entry and label
lbl_email=Label(root,text="EMAIL",font=("ariel",19,"bold"),fg="red",bg="whitesmoke").place(x=70,y=130,height=50,width=100)
txt_email=Entry(root,textvariable=var_email,font=("times new roman",15,"bold"),bg="ivory3",fg="black").place(x=250,y=140,height=30,width=400)

# Gender label and radio button selection
lba_gender=Label(root,text="GENDER ",font=("ariel",19,"bold"),fg="red",bg="whitesmoke").place(x=70,y=180,height=50,width=130)
male=Radiobutton(root,text="Male",value="male",variable=var_gender,font=("ariel",15,"bold"),fg="firebrick3",bg="whitesmoke").place(x=280,y=185)
female=Radiobutton(root,text="Female",value="female",variable=var_gender,font=("ariel",15,"bold"),fg="firebrick3",bg="whitesmoke").place(x=430,y=185)
var_gender.set("male")     # setting default selection to male

# Checkbutton 
check_=Checkbutton(root,text="Accept our Terms and Condition",onvalue="1",offvalue="0",variable=var_check,font=("ariel",13,"bold"),fg="Indianred4",bg="whitesmoke").place(x=250,y=250)
var_check.set("0")         
btn=Button(root,text="SHOW",font=("times new roman",20,"bold"),bg="black",fg="orange red",command=get_data).place(x=290,y=305,width=200,height=40)

#Display output result 
lbl_result=Label(root,text="",font=("Verdana",16,),fg="coral",bg="whitesmoke")
lbl_result.place(x=0,y=380,relwidth=1)

root.mainloop()