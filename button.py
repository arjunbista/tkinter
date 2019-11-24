from tkinter import*
def click():
    txt.set("You just Clicked.")
root=Tk()
root.geometry('400x450')
root.config(background='black')
txt=StringVar()
var2=Label(root,textvariable=txt)
var2.config(font=("Arial",25),fg='blue')
var2.pack()
but1=Button(root,text="Click Here",font=(" ",20),command=click)
but1.pack(padx=(10,18),pady=(10,18))
root.mainloop()