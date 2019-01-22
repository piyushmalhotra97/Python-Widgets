from tkinter import*

a=Tk()
a.title("The Avengers")
a.geometry("500x500+0+0")

def fun1():
    print("The Soldier")
    
B1 = Button(a,text = "Steve",width = 5,height = 5, bd = 5,
            fg="Silver",bg = "Blue",command = fun1, relief = GROOVE)
B1.pack(side=TOP,fill=X,padx=10,ipadx=40,ipady=30)

a.mainloop()
