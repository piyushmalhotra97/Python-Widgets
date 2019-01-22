from tkinter import*

a=Tk()
a.title("Table")
a.geometry("500x500+0+0")

    
B1 = Button(a,text = "Steve",width = 5,height = 5, bd = 5,fg="Silver",bg = "Navy")
B2 = Button(a,text = "Tony",width = 5,height = 5, bd = 5,fg="Red",bg = "Yellow")
B3 = Button(a,text = "Bruce",width = 5,height = 5, bd = 5,fg="Black",bg = "Green")
B4 = Button(a,text = "Thor",width = 5,height = 5, bd = 5,fg="Yellow",bg = "Black")
B5 = Button(a,text = "Widow",width = 5,height = 5, bd = 5,fg="Maroon",bg = "Black")
B6 = Button(a,text = "T'challa",width = 5,height = 5, bd = 5,fg="Silver",bg = "Black")
B7 = Button(a,text = "Peter",width = 5,height = 5, bd = 5,fg="Red",bg = "Blue")
B8 = Button(a,text = "Scott",width = 5,height = 5, bd = 5,fg="Silver",bg = "Red")
B9 = Button(a,text = "Clint",width = 5,height = 5, bd = 5,fg="Black",bg = "Yellow")
B10 = Button(a,text = "Wanda",width = 5,height = 5, bd = 5,fg="Red",bg = "Green")
B11 = Button(a,text = "Vision",width = 5,height = 5, bd = 5,fg="Silver",bg = "Blue")
B12 = Button(a,text = "Thanos",width = 5,height = 5, bd = 5,fg="Silver",bg = "Blue")
B13 = Button(a,text = "Loki",width = 5,height = 5, bd = 5,fg="Silver",bg = "Blue")

B1.grid(row=0,column=0)
B2.grid(row=0,column=1)
B3.grid(row=0,column=2)
B4.grid(row=1,column=0)
B5.grid(row=1,column=1)
B6.grid(row=1,column=2)
B7.grid(row=2,column=0)
B8.grid(row=2,column=1)
B9.grid(row=2,column=2)
B10.grid(row=3,column=0)
B11.grid(row=3,column=1)
B12.grid(row=3,column=2)
B13.grid(row=4,column=0)


a.mainloop()
