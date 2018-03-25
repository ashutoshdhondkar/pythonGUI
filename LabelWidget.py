# wap that displays label "welcome from python" when you click on button

from tkinter import *

class MyGui:
    def __init__(self,root):
        self.root=root
        
        # creating a frame
        self.frame=Frame(self.root,bg="blue",height=500,width=500,cursor="cross")
        self.frame.pack()
        self.frame.propagate(0)
        
        # now we need to create some buttons
        self.enterButton = Button(self.frame,text="Enter into python",command = lambda: self.ClickButton(1))
        self.exitButton = Button(self.frame,text="quit",command= lambda : self.ClickButton(2))
        # since we cannot use parenthesis in command option we will not be able to pass the parameters
        # hence we use a lambda function which will call the methods into it and give it to command
        
        
        # creating a grid for buttons
        self.enterButton.grid(row=0,column=12)
        self.exitButton.grid(row=0,column=11,padx=10)
        
    # creating an event handling function
    def ClickButton(self,num):
        if(num==1):
            self.label=Label(self.frame,text="Welcome from python",font=('Times',50,'bold italic'))
            self.label.grid(columnspan=5)
                        
        elif(num == 2):
            exit()
# class defined

root=Tk()   # created a root window

obj=MyGui(root) # created an object of our defined class

root.mainloop()
                
    