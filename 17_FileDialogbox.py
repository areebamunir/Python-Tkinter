# Different filedialog operations

from tkinter import *
from tkinter import filedialog
root=Tk()
root.geometry("600x500+100+50")
def openFiles():
    # op=filedialog.askdirectory(title="Select Folder")
    # op=filedialog.askopenfile(title="Select Folder")
    #op=filedialog.askopenfilename(title="Select Folder")
    #print(op.split("/")[-1])        -----to select file name
    #op=filedialog.askopenfilenames(title="Select Folder")
    #op=filedialog.askopenfiles(title="Select Folder")
    #op=filedialog.asksaveasfile(title="Select Folder",filetypes=(("text file",".txt"),("all files","*")))
    op=filedialog.asksaveasfilename(title="Select Folder",filetypes=(("text file",".txt"),("all files","*")))
    print(op)

btn=Button(root,text="FileDialog",command=openFiles).place(x=50,y=50)

root.mainloop()