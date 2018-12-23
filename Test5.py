from tkinter import *

app=Tk()

def hel():
    print("Hello")

menubar=Menu(app)

#file menu drop down
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=hel)
#nested open menu
open_nest=Menu(filemenu)
open_nest.add_command(label='/C')
open_nest.add_command(label='/D')
open_nest.add_command(label='/E')
filemenu.add_cascade(label='Open',menu=open_nest)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=app.quit)
menubar.add_cascade(label="File", menu=filemenu)

#edit menu drop down
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="Copy", command=hel)
editmenu.add_command(label='Cut', command=hel)
editmenu.add_command(label='Paste',command=hel)
menubar.add_cascade(label='Edit',menu=editmenu)

#helpmenu
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label='About us')
ser=Menu(helpmenu)
ser2=Menu(ser)
ser2.add_command(label='Email us')
ser2.add_command(label='Post us')
ser.add_cascade(label='Write to us',menu=ser2)
helpmenu.add_cascade(label='Contact us',menu=ser)
helpmenu.add_command(label='Visit Our Website')
menubar.add_cascade(label='Help',menu=helpmenu)
app.config(menu=menubar)
mainloop()
