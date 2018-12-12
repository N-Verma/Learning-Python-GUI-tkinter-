import tkinter as tk //the module is been imported and given a short name tk
r = tk.Tk() //the command Tk() is used to stablish a main working windows for the app
r.title("TEST 1") //name of the app
button1=tk.Button(r,text='Start',width=25,bg='red') //Button() fucntion is used to create a button with parameters width and background colour.
button2=tk.Button(r,text='Stop',width=25,bg='blue')
button1.pack() //specifies the geometric positon of the button
button2.pack()
r.mainloop() //the app is  runned in a infinite loop using this command mainloop()
