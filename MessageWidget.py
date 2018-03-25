# program to print a multi line message on screen

# we use Message to display text in multiple lines
# whereas Label will display all the text in single line

from tkinter import *

# lets wrap all the methods into a single class
class MyGui:
    # let's now define a constructor
    def __init__(self,root):
        self.root=root
        self.frame=Frame(self.root,bg="blue",height=500,width=500)
        # now we have created a frame
        self.frame.pack()
        # we need to pack it on root window
        self.frame.propagate(0)
        # so that the frame will not shrink
        
        # now lets just type a message to be displayed on the root window
        self.m=Message(self.frame,text="hello this is ashutosh. I am from sies gst,nerul",bg="blue",font=('Times',30,'bold italic'))
        
        self.m.pack()
        # packed the message on frame
        
root=Tk()   # created a root window
root.title("Moodle")
obj=MyGui(root)


root.mainloop()