# program to create a frame in root window

# Frame is similar to canvas that represents a rectangular area where some text or
# widgets can be displayed. 

from tkinter import *

root=Tk()   # root window created
root.title("MoodleWorkspace")
#giving title to created window


f=Frame(root,height=1360,width=768,bg="blue",cursor="cross")
#    cursor indicates the type of the cursor to be displayed on the frame


f.pack()
# attach the frame to root window

root.mainloop()
# let the root window wait for any events