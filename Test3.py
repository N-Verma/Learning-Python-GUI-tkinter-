from tkinter import *

window = Tk()
ok = Button(text='OK',bg='GREEN')
stop = Button(text='STOP',bg='red')

ok.pack(side=RIGHT,padx=10,pady=6) //postion of the button is taken from the right side
stop.pack(side=LEFT,padx=10,pady=6) //position of the button is taken from the left side
mainloop()
