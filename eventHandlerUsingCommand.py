# wap to create a button and bind it with an event handler function using command option
from tkinter import *

def clickbutton():
    print("hello world!")

root=Tk()   #root window created

root.title("Event Handling")
# given title to root window

frame=Frame(root,height=500,width=600,bg="blue")
frame.pack()
frame.propagate(0)
# propagate(0) is used so that the frame will not shrink

#created a frame and packed it into root window


b=Button(frame,height=5,width=4,fg="yellow",text="click me",activeforeground="red",bg="black",command=clickbutton)
# binded the button with event handler function

b.pack()
root.mainloop()