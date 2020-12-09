#maziyar adibifar
#https://www.aparat.com/v/Oy7Wp
from tkinter import *
root=Tk()
root.title("maziyar adibifar")
l1=Label(root,text="name ???")
l1.pack()

e=Entry(root,width=50)
e.pack()

def click():
    global r
    r=Label(root,text=e.get())
    r.pack()
    b1['state']=DISABLED
    b2['state']=NORMAL
def dell():
    r.destroy()
    b1['state']=NORMAL
    b2['state']=DISABLED
b1=Button(root,text="enterr",command=click)
b1.pack()
b2=Button(root,text="clear",command=dell,state=DISABLED)
b2.pack()





root.mainloop()