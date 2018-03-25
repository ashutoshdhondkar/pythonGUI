# working with buttons on grid

from tkinter import *

root=Tk()   #created a root window


# creating buttons to be placed in grid
button1=Button(root,text="button-1",bg="yellow",fg="blue")
button2=Button(root,text="button-2",bg="yellow",fg="red")
button3=Button(root,text="button-3",bg="yellow",fg="black")
button4=Button(root,text="button-4",bg="yellow",fg="purple")

# creating grid
button1.grid(row=0,column=0,padx=10,pady=10)
# padx and pady options are used to give indicate how much space should be left around component
# horizontally and vertically (respectively)
button2.grid(row=0,column=1)
button3.grid(row=0,column=2,padx=60,pady=10)
button4.grid(row=1,column=1)
# we don't need to use pack once we placed the buttons in a grid

root.mainloop()