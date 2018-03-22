from tkinter import *

root = Tk() #creating a window

#create a canvas as a child to root window
c=Canvas(root,bg="blue",height=700,width=1200,cursor='pencil')

#create a line in canvas
id=c.create_line(50,50,200,50,200,150,width=4,fill="white")
#create_line returns an identification number
# parameters(x1,y1,x2,y2,x3,y3)

#create a oval in canvas
id=c.create_oval(100,100,400,300,width=5,fill="red",outline="black",activefill="green")
# activefill will chnage the color of rectangle from red to green as soon as our mouse pointer is kept 
# on oval

# create a polygon in canvas
id=c.create_polygon(10,10,200,200,300,200,width=3,fill="green",outline="red",activefill="blue",smooth=0)

#smooth is either 0 or 1
# 0 indicates that the polygon has sharp edges
# 1 indicates that the polygon has smooth edges

#create a rectangle in canvas

id=c.create_rectangle(500,200,700,600,width=5,fill="gray",outline="black",activefill="red")
# it takes the same parameter as that of rectangle function in c

#creating an arc
id=c.create_arc(400,400,600,600, width=5,start=0,extent=270,style="arc")

#style=arc does not display the symmetry lines
# if we don't specify this then it will show symmetry lines along with arc

#create some text in canvas
fnt=('Times',40,'bold italic')
id=c.create_text(500,100,text="this is my first lecture on GUI",font=fnt,fill="yellow",activefill="red")

c.pack()

root.mainloop()