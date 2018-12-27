#this game shows a name of a colour with its font colour other thans it's name, the player has to
#choose the colour of the text from the given colour palette

from tkinter import *
import random

score = 0
time = 30
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','Purple','Brown']
def start_game(event):
    if time <= 30:
        countdown()
    press()

def countdown():
    global  time
    if time >0:
        time1=time-1
        timelabel.config(text='Timeleft:'+str(time1))
        timelabel.after(1000,time1)
def press(col):
    global score
    if time>0:
        if col.lower()==colours[1].lower():
            score+=1
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scorelabel.config(text='Score:' + str(score))
app = Tk()
app.title('Colour game')
app.geometry('375x375')
instructions = Label(app, text = "Press the colour of the words, and not the word text!",
                             font = ('Helvetica', 12))
instructions.grid()
scorelabel = Label(app, text="Press enter to start",font=('Helvetica', 12))
scorelabel.grid()
timelabel = Label(app, text="Time left: " + str(time), font=('Helvetica', 12))
timelabel.grid()
label = Label(app, font=('Helvetica', 60))
label.grid()

app.bind('<Return>',start_game)

f1=Frame(app)
f1.grid()
b1=Button(f1,bg='red',width=4,height=2,command=lambda: press('red')).grid(row=8,column=1)
b2=Button(f1,bg='green',width=4,height=2,command=lambda: press('green')).grid(row=8,column=2)
b3=Button(f1,bg='blue',width=4,height=2,command=lambda: press('blue')).grid(row=8,column=3)
b4=Button(f1,bg='brown',width=4,height=2,command=lambda: press('brown')).grid(row=9,column=1)
b5=Button(f1,bg='yellow',width=4,height=2,command=lambda: press('yellow')).grid(row=9,column=2)
b6=Button(f1,bg='pink',width=4,height=2,command=lambda: press('pink')).grid(row=9,column=3)
b7=Button(f1,bg='black',width=4,height=2,command=lambda: press('black')).grid(row=10,column=1)
b8=Button(f1,bg='orange',width=4,height=2,command=lambda: press('orange')).grid(row=10,column=2)
b9=Button(f1,bg='purple',width=4,height=2,command=lambda: press('purple')).grid(row=10,column=3)

mainloop()
