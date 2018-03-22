# this program will load an image onto canvas

from tkinter import *

root=Tk()   #window created

# now we need to copy the image into a particular file
# this is done by using PhotoImage class
file1=PhotoImage(file="ashutosh.gif") 
# loaded/copied the image named sachin.jpg in file1
file2=PhotoImage(file="DANCING_BABY.gif")

# i have tried jpg files but it did't work
# maybe it can only read gif files

# creating an object of canvas
c=Canvas(root,bg="blue",height=700,width=600,cursor="pencil")

# load the image onto the canvas
# this is done by using create_image() method
id=c.create_image(500,200,anchor=NE,image=file1,activeimage=file2)

#let's create some text

id=c.create_text(300,500,text="hello gif",font=('Times',50,'bold italic underline'))


c.pack()

root.mainloop()
