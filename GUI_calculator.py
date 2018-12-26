from tkinter import *

exp=""  #global declaration of the variable

def press(num):  #function to create an equation suing the buttons pressed
    global exp
    exp=exp+str(num)
    eq.set(exp)

def eqpress():  #function to execute on "= press, try and except is used to show errors in case of division by 0
    try:
        global exp
        total=str(eval(exp))
        eq.set(total)
        exp=""
    except:
        eq.set('error 404')
        exp=""

def clear():
    global exp
    exp = ""
    eq.set("")

if __name__ == "__main__":
    app=Tk()
    app.configure(bg='light green')
    app.title('Calculator')
    app.geometry('265x125')

    eq=StringVar() #StringVar is a variable class,these are defined in the tkinter module and are used like normal python variable

    exp_field=Entry(app,textvariable=eq)
    exp_field.grid(columnspan=4,ipadx=70)

    eq.set('Enter ur exp')

    b1=Button(app,text='1',fg='black',bg='red',command=lambda:press(1),height=1,width=7).grid(row=2,column=0)
    b2 = Button(app, text='2', fg='black', bg='red', command=lambda: press(2), height=1, width=7).grid(row=2, column=1)
    b3 = Button(app, text='3', fg='black', bg='red', command=lambda: press(3), height=1, width=7).grid(row=2, column=2)
    b4 = Button(app, text='4', fg='black', bg='red', command=lambda: press(4), height=1, width=7).grid(row=3, column=0)
    b5 = Button(app, text='5', fg='black', bg='red', command=lambda: press(5), height=1, width=7).grid(row=3, column=1)
    b6 = Button(app, text='6', fg='black', bg='red', command=lambda: press(6), height=1, width=7).grid(row=3, column=2)
    b7 = Button(app, text='7', fg='black', bg='red', command=lambda: press(7), height=1, width=7).grid(row=4, column=0)
    b8 = Button(app, text='8', fg='black', bg='red', command=lambda: press(8), height=1, width=7).grid(row=4, column=1)
    b9 = Button(app, text='9', fg='black', bg='red', command=lambda: press(9), height=1, width=7).grid(row=4, column=2)
    b0 = Button(app, text='0', fg='black', bg='red', command=lambda: press(0), height=1, width=7).grid(row=5, column=0)

    plus = Button(app, text='plus', fg='black', bg='red', command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
    minus = Button(app, text='minus', fg='black', bg='red', command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
    multiply = Button(app, text='multiply', fg='black', bg='red', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
    divide = Button(app, text='divide', fg='black', bg='red', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
    equal = Button(app, text='=', fg='black', bg='red', command=eqpress, height=1, width=7)
    equal.grid(row=5, column=2)
    clear = Button(app, text='clear', fg='black', bg='red', command=clear, height=1, width=7)
    clear.grid(row=5, column=1)

    mainloop()
