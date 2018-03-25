# working with buttons in place layout manager

from tkinter import *

root=Tk()   #created a root window


# creating buttons to be placed in grid
button1=Button(root,text="button-1",bg="yellow",fg="blue")
button2=Button(root,text="button-2",bg="yellow",fg="red")
button3=Button(root,text="button-3",bg="yellow",fg="black")
button4=Button(root,text="button-4",bg="yellow",fg="purple")

#placing created buttons at specified points or pixels
button1.place(x=90,y=10,height=50,width=50)
button2.place(x=30,y=10,height=100,width=100)
button3.place(x=100,y=90,height=90,width=60)
button4.place(x=150,y=150,height=100,width=150)
# we don't need to use pack when using place layout manager

# even if we give height and width while creating a button and if we specify height and width
# in place() then the height and width of place will be considered
# eg.
#    button4=Button(root,text="button-4",bg="yellow",fg="purple",height=50,width=50)
#    button4.place(x=150,y=150,height=100,width=150)

# here in this case height=100 and width =150 is considered

root.mainloop()