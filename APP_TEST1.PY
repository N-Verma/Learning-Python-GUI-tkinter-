from tkinter import *

app=Tk()

area = Canvas(app,height=200,width=200)
area.pack()
area.create_line(10,10,10,100,90,100,90,10,10,10,fill='red')
area.create_rectangle(10,50,90,150)
area.create_oval(10,50,90,150)

b1=Button(app,text='Start',bg='green',width=25,activebackground="yellow")
b1.pack(side="right",padx=10,pady=0)

b2=Button(app,text='Stop',bg='red',width=25,activebackground="yellow")
b2.pack(side="left",padx=10,pady=6)
mainloop()
