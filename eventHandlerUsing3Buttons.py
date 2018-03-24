# a python program that creates three push buttons and change the background of the frame
# according to button clicked by user

from tkinter import *

class EventHandler:
    def __init__(self,root):
        self.frame=Frame(root,height=500,width=500)
        self.frame.propagate(0)
        # so that the frame should not shrink
        self.frame.pack()
        
        b1=Button(self.frame,text="yellow",height=3,width=6,bg="yellow",command = lambda : self.click(1))
        b2=Button(self.frame,text="RED",height = 3,width=6,bg="red",command = lambda : self.click(2))
        b3=Button(self.frame,text="green",height=3,width=6,bg="green",command = lambda : self.click(3))
        b1.pack()
        b2.pack()
        b3.pack()
    

                
    def click(self,num):
        if(num == 1):
            self.frame["bg"] = "yellow"
        elif(num == 2):
            self.frame["bg"] = "red"
        elif(num==3):
            self.frame["bg"] = "green"
        print("You just clicked!")
            
root=Tk()   # root window created

gui=EventHandler(root)

root.mainloop()
        