import turtle

Min_len = 5

#stupid functions
def square(t1, side):
    for x in range(4):
        t1.forward(side)
        t1.left(90)

def hexagon(t1, side):
    for x in range(6):
        t1.forward(side)
        t1.left(60)

def triangle(t1, side):
    for x in range(3):
        t1.forward(side)
        t1.left(120)

#recursive function
def recfunc(t, len, iter):
    if(len > Min_len):
        t.circle(len)

        #carry forward
        new_len = len - iter
        recfunc(t, new_len, iter)


#initiation
t = turtle.Turtle()
t.setheading(0)
t.color('white')
#t.hideturtle()
sc = turtle.getscreen()
sc.bgcolor('black')
#sc.tracer(100)
t.speed(0)

#Code to do things
recfunc(t, 500, 5)

turtle.mainloop()