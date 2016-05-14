import turtle

# draws a box
def box1():
    Fred = turtle.Turtle()
    Fred.forward(50)
    Fred.left(90)
    Fred.forward(50)
    Fred.left(90)
    Fred.forward(50)
    Fred.left(90)
    Fred.forward(50)
    turtle.done()


# draws a box using a loop
def box2():
    Fred = turtle.Turtle()
    for i in range(4):
        print i
        Fred.forward(50)
        Fred.left(90)
    turtle.done()



# draws a box with the given size
def box3(size):
    Fred = turtle.Turtle()
    for i in range(4):
        print i
        Fred.forward(size)
        Fred.left(90)
    turtle.done()



# draws a shape with angles based on the number of sides
# draws a shape with the given size
def box4(sides, size):
    Fred = turtle.Turtle()
    for i in range(sides):
        print i
        Fred.forward(size)
        Fred.left(360/sides)
    turtle.done()
box4(7,125)
