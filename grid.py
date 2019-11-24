from tkinter import*
root=Tk()
root.geometry('400x500')
var=Label(root,text='Hey,Bro!').grid(row=0,column=0)
var=Label(root,text="Alright, Then.")
var.grid(row=0,column=1)
root.resizable(0,0)   #This does not let the USER to resize window because(0,0)#
root.mainloop()