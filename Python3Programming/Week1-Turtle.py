# Week 1 - Our first Turtle Program
import turtle          # use Turtle library

# wn = turtle.Screen()   # creates a graphics window
# alex = turtle.Turtle() # create a turtle named alex
# alex.forward(150)      # tell alex to move forward by 150 units
# alex.left(90)          # turn by 90 degrees
# alex.forward(75)       # completes the second side of a rectange
# alex.left(90)
# alex.forward(150)
# alex.left(90)
# alex.forward(75)
# wn.exitonclick()       # force window to not auto-close once done
#
# alex.salary = 50000
# print(alex.salary)

# L-shape
# wn = turtle.Screen()
# ella = turtle.Turtle()
# ella.right(90)
# ella.forward(150)
# ella.left(90)
# ella.forward(75)
# wn.exitonclick()

# Checkmark
# wn = turtle.Screen()
# maria = turtle.Turtle()
# maria.right(45)
# maria.forward(75)
# maria.left(90)
# maria.forward(150)
# wn.exitonclick()

# Draw left line
# wn = turtle.Screen()
# james = turtle.Turtle()
# james.left(180)
# james.forward(75)
# wn.exitonclick()

# Attributes
# Colour names: https://www.w3schools.com/colors/colors_names.asp
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("Linen")        # set the window background color
#
# tess = turtle.Turtle()
# tess.color("LightSeaGreen")              # make tess blue
# tess.pensize(3)                 # set the width of her pen
#
# tess.forward(50)
# tess.left(120)
# tess.forward(50)
#
# wn.exitonclick()                # wait for a user click on the canvas

# capital T
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("Green")
# sherna = turtle.Turtle()
# sherna.color("White")
# sherna.pensize(10)
#
# sherna.left(90)
# sherna.forward(150)
# sherna.left(90)
# sherna.forward(50)
# sherna.right(180)
# sherna.forward(100)
# wn.exitonclick()

# Instances: A Herd of Turtles
# import turtle
# wn = turtle.Screen()             # Set up the window and its attributes
# wn.bgcolor("lightgreen")
#
#
# tess = turtle.Turtle()           # create tess and set his pen width
# tess.pensize(5)
#
# alex = turtle.Turtle()           # create alex
# alex.color("hotpink")            # set his color
#
# tess.forward(80)                 # Let tess draw an equilateral triangle
# tess.left(120)
# tess.forward(80)
# tess.left(120)
# tess.forward(80)
# tess.left(120)                   # complete the triangle
#
# tess.right(180)                  # turn tess around
# tess.forward(80)                 # move her away from the origin so we can see alex
#
# alex.forward(50)                 # make alex draw a square
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
# alex.forward(50)
# alex.left(90)
#
# wn.exitonclick()

# For-loops
# import turtle
# wn = turtle.Screen()
#
# elan = turtle.Turtle()
#
# distance = 50
# angle = 90
# for _ in range(10):
#     elan.forward(distance)
#     elan.right(angle)
#     distance = distance + 10
#     angle = angle - 3
# wn.exitonclick()

# Spiral
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# tess = turtle.Turtle()
# tess.color("blue")
# tess.shape("turtle")
#
# dist = 5
# tess.up()                     # this is new
# for _ in range(30):    # start with size = 5 and grow by 2
#     tess.stamp()                # leave an impression on the canvas
#     tess.forward(dist)          # move tess along
#     tess.right(24)              # and turn her
#     dist = dist + 2
# wn.exitonclick()

# Stamping Example 2
# import turtle
# wn = turtle.Screen()
# jose = turtle.Turtle()
# jose.shape("turtle")
# jose.penup()
#
# for size in range(10):
#     jose.forward(50)
#     jose.stamp()
#     jose.forward(-50)
#     jose.right(36)
# wn.exitonclick()

# Stamping Example 3
# import turtle
# wn = turtle.Screen()
# jose = turtle.Turtle()
# jose.shape("circle")
# jose.penup()
#
# for size in range(3):
#     jose.forward(50)
#     jose.stamp()
# wn.exitonclick()

# The random module
# import random
#
# #  returns a floating point number in the range [0.0, 1.0)
# prob = random.random()
# print(prob)
#
# diceThrow = random.randrange(1,7)       # return an int, one of 1,2,3,4,5,6
# print(diceThrow)

