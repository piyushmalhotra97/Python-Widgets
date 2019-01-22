#sudo apt-get install python-tk
from tkinter import *
a=Tk()
a.geometry("800x500+30+30")
a.title("Shopping Cart")


B1=Button(a,text="Day",width=20,height=6)
B2=Button(a,text="Seminar",width=80,height=2)
B3=Button(a,text="Schedule",width=40,height=2)
B4=Button(a,text="Begin",width=20,height=2)
B5=Button(a,text="End",width=20,height=2)
B6=Button(a,text="Topic",width=40,height=4)
B7=Button(a,text="Monday",width=20,height=4)
B8=Button(a,text="8:00 a.m.",width=20,height=4)
B9=Button(a,text="5:00 p.m.",width=20,height=4)
B10=Button(a,text="Introduction to XML",width=40,height=2)
B11=Button(a,text="Validity: DTD and Relax NG",width=40,height=2)
B12=Button(a,text="Tuesday",width=20,height=6)
B13=Button(a,text="8:00 a.m.",width=20,height=2)
B14=Button(a,text="11:00 a.m.",width=20,height=2)
B15=Button(a,text="11:00 a.m.",width=20,height=2)
B16=Button(a,text="2:00 p.m.",width=20,height=2)
B17=Button(a,text="2:00 p.m.",width=20,height=2)
B18=Button(a,text="5:00 p.m.",width=20,height=2)
B19=Button(a,text="XPath",width=40,height=2)
B20=Button(a,text="XSL Transformation",width=40,height=2)
B21=Button(a,text="Wednesday",width=20,height=2)
B22=Button(a,text="8:00 a.m.",width=20,height=2)
B23=Button(a,text="12:00 p.m.",width=20,height=2)
B24=Button(a,text="XSL Formatting Objects",width=40,height=2)

B1.grid(row=0,column=0,rowspan=3)
B2.grid(row=0,column=1,columnspan=3)
B3.grid(row=1,column=1,columnspan=2)

B4.grid(row=2,column=1)
B5.grid(row=2,column=2)

B6.grid(row=1,column=3,rowspan=2)

B7.grid(row=3,column=0,rowspan=2)
B8.grid(row=3,column=1,rowspan=2)
B9.grid(row=3,column=2,rowspan=2)
B10.grid(row=3,column=3)
B11.grid(row=4,column=3)

B12.grid(row=5,column=0,rowspan=3)
B13.grid(row=5,column=1)
B14.grid(row=5,column=2)
B15.grid(row=6,column=1)
B16.grid(row=6,column=2)
B17.grid(row=7,column=1)
B18.grid(row=7,column=2)

B19.grid(row=5,column=3,sticky=W+E+N+S)
B20.grid(row=6,column=3,sticky=W+E+N+S)
B21.grid(row=8,column=0)
B22.grid(row=8,column=1)
B23.grid(row=8,column=2)
B24.grid(row=8,column=3)
a.mainloop()


