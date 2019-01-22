from tkinter import*
from tkinter import messagebox
master=Tk()
master.geometry("500x500+30+30")
master.title("ITRONIX SOLUTIONS")
def check():
	e=entry1.get()	
	p=entry2.get()
	if e=="itronix" and p=="123456":
		messagebox.showinfo("Login Successfully", "Access Granted")
	else:
		messagebox.showinfo("Invalid Password", "Try Again")
lbl = Label(master, text="Welcome to Itronix Solution",font=("Helvetica", 16))
lbl.grid(row=0,column=0,columnspan=2)
label=Label(master, text="Email: ")
label.grid(row=1,sticky="w")
entry1 = Entry(master)
entry1.grid(row=1,column=1)

label=Label(master, text="Password: ")
label.grid(row=2,sticky="w")
entry2 = Entry(master)
entry2.grid(row=2,column=1)

c1=Button(master,text = "Submit",command=check)
c1.grid(row=3,column=0,columnspan=2)

master.mainloop()
