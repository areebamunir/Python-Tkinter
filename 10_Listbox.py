from tkinter import *
root=Tk()
root.title("Python GUI")
root.geometry("800x500+200+80")
#root.config(bg="#262626")
root.resizable(False,False)


#-------use with insertion in a list---------
#def get_language():
#    get_cursor=language_list.curselection()
    # print(language_list.get(0))
    # print(get_cursor,language_list.get(get_cursor))
#    print(get_cursor)
#    for i in get_cursor:
#        print(language_list.get(i))

# to delete certain value from list

#--------use this for delete any item in list---------
def get_language():
    get_cursor=language_list.curselection()
    # print(language_list.get(0))
    # print(get_cursor,language_list.get(get_cursor))
    print(get_cursor)
    #for i in get_cursor:
    #   print(language_list.get(i))
    language_list.delete(get_cursor)



#different select mood by default is browse
#language_list=Listbox(root,font=("ariel",15),bg="#262626",fg="white",justify=CENTER,selectmode=MULTIPLE)
language_list=Listbox(root,font=("ariel",15),bg="#262626",fg="white",justify=CENTER,selectmode=EXTENDED)
language_list.place(x=100,y=50,width=150)

btn=Button(root,text="SHOW",command=get_language,font=("times new roman",20),bg="green",fg="white").place(x=120,y=320,height=30)

for i in range(0,20):
    language_list.insert(i,"Language: "+str(i))
root.mainloop()