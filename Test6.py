#scroll bar
from tkinter import *

app=Tk()
sb=Scrollbar(app)
sb.pack(side=RIGHT,fill=Y)
lb=Listbox(app,yscrollcommand=sb.set)
for i in range(50):
    lb.insert(END,i)
lb.pack(side=LEFT,fill=BOTH)
sb.config(command=lb.yview)

mainloop()
