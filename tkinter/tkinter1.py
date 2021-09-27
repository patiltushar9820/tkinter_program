import tkinter
from tkinter import *
root=Tk()

e=Entry(root,width=50)
e.pack()
e.insert(0,"Enter Your Name")

#function defination
def myClick():
    myLabel2=Label(root,text="Hello "+e.get())
    myLabel2.pack()


mylabel1=Label(root,text='Welcome in GoDigital ')
button=Button(root,text='Enter Your Name ',command=myClick)

#showing it onto window
mylabel1.pack()
button.pack()

root.mainloop()