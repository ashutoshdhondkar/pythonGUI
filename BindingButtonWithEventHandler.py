# write a program to create a push button and bind it with an 
# event handler function

from tkinter import *

# defining a function that handles a particular event
def buttonClick(self):
    print("hello you have clicked me!!!")


root=Tk()   #root window created
# now we first need to create a frame where our button is to be placed
# creating frame object / frame
f=Frame(root,bg="blue",height=800,width=700)

# now  we need to create buttons
# creating button object/button
b=Button(f,text="click me!",height=5,width=10,bg="yellow",fg="red",fill="black")

# now we need to bind the button with some function
# this is called as event handling


b.pack()

b.bind('<Button-1>',buttonClick)
# <button-1> indicates the first key of mouse


f.pack()


root.mainloop()