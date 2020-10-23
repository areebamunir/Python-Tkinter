# Scale

from tkinter import *
root=Tk()
root.title("Scale")
root.geometry("800x500+200+80")
root.config(bg="#262626")
root.resizable(False,False)
def get_price(price_):
    lbl_result.config(text=str(price.get()))
    # or
    #lbl_result.config(text=str(price_))

price=Scale(root,from_=50,to=250,orient=HORIZONTAL,command=get_price,length=700,sliderlength=100,showvalue=FALSE)
price.place(x=50,y=50,width=700)

lbl_result=Label(root,bg="#262626",fg="white")
lbl_result.place(x=0,y=100,relwidth=1)
root.mainloop()