from tkinter import *
r=Tk()
c=Canvas(r,width=200,height=200) //canvas function is used to create various geometric shapes
c.pack()
c.create_line(10,10,10,100) // the 4 number are taken in pair of 2 from the left side, yhey represent the coordinate of the 2 end of the line
                            //(0,0) point is located at the top-left most corner of the canvas
c.create_line(10,10,10,100,90,100,90,10,10,10) //this will make a square of side 90, with its points at (10,10) (10,100), (90,100),(90,100)
c.create_rectangle(10,20,100,80) //these 4 points taken in pair represent the location on the endpoints of the diagonal of the rectangle

//coloring the rectangle
c.create_rectangle(10,20,100,80,fill"#fb0")
mainloop()
