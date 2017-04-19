import turtle               # import everything from the turtle module
canvas = turtle.Screen()    # get a canvas to draw on
canvas.setup(400,200)       # set the canvas width and height
poopyhead = turtle.Turtle() # create a new turtle named poopyhead
poopyhead.shape("turtle")   # set poopyhead's shape
poopyhead.color("purple")   # set poopyhead's color to purple
poopyhead.forward(50)       # move poopyhead forward by 50 pixels
poopyhead.left(90)          # move poopyhead forward by 100 pixels
turtle.done()
