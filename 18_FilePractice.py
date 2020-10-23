from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
root=Tk()
root.geometry("600x500+100+50")
def openFiles():
    op=filedialog.askopenfile(title="Select file",filetypes=(("text file",".txt"),))
    if op!=None:
        lbl_name.config(text="FileName:  "+str(op.name.split("/")[-1]))
        var_filename.set(str(op.name))
        for i in op:
            txt_area.insert(END,str(i))
    op.close()

def saveAs():
    op=filedialog.asksaveasfile(title="Save As",filetypes=(("text file",".txt"),))
    if op!=None:
        var_filename.set(str(op.name))
        lbl_name.config(text="FileName:  "+str(op.name.split("/")[-1]))
        op.write(txt_area.get("1.0",END))
        op.close()
        messagebox.showinfo("Save As","File has been saved")

def save_file():
    if var_filename.get()=="":
        saveAs()
    else:
        op=open(var_filename.get(),"w")
        op.write(txt_area.get("1.0",END))
        op.close()
        messagebox.showinfo("Save","File has been saved")

var_filename=StringVar()

btn=Button(root,text="Open",command=openFiles).place(x=50,y=50,width=100)
btn=Button(root,text="Save",command=save_file).place(x=150,y=50,width=100)
btn=Button(root,text="Save As",command=saveAs).place(x=250,y=50,width=100)

lbl_name=Label(root,text="FileName",font=("times new roman",15))
lbl_name.place(x=50,y=100)
txt_area=Text(root,font=("times new roman",15),bd=2,relief=RIDGE)
txt_area.place(x=50,y=130,width=400,height=250)

root.mainloop()