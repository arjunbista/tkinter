#TASK 8#
from tkinter import*
def click():
    txt.set("You just Clicked.")
root=Tk()
root.geometry('400x450')
root.config(background='black')
txt=StringVar()
txt.set("Hi There!, welcome bro.")
var2=Label(root,textvariable=txt)
var2.config(font=("Arial",20),fg='blue')
var2.pack()
but1=Button(root,text="Click Here",font=(" ",20),command=click)
#root.iconbitmap("ball.ico")
Img=PhotoImage(file='bird.gif')
logo=PhotoImage(file='rss.gif')
sign=logo.subsample(1,1)
but1.config(image=sign,compound=LEFT)
but1.pack(padx=(10,18),pady=(10,18))
root.mainloop()

