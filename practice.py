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

# fuckin draws a grid of dots using a loop in a loop
def grid1():
    Fred = turtle.Turtle()
    for row in range(10):
        #this loop draws the row
        for column in range(10):
            Fred.dot()
            Fred.penup()
            Fred.forward(20)
        Fred.back(20 * 10)
        Fred.right(90)
        Fred.forward(20)
        Fred.left(90)
    turtle.done()

# draws a grid of fuckin dots
# uses parameters (rows,dots,ect) instead of values
# size means distance between dots
def grid2(rows,dots,size = 40):
    Fred = turtle.Turtle()
    for row in range(rows):
        #this loop draws the row
        for column in range(dots):
            Fred.dot()
            # the penup command can be before the loop
            Fred.penup()
            Fred.forward(size)
        # gets Fred in place for the next row
        Fred.back(size * dots)
        Fred.right(90)
        Fred.forward(size)
        Fred.left(90)
    turtle.done()
grid2(20,15,10)
