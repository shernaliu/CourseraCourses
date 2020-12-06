# Assignment 1: Turtle drawing - shark
import turtle

wn = turtle.Screen()
wn.bgcolor("SteelBlue")
t = turtle.Turtle()
t.pensize(5)
t.speed(10)
t.shape("arrow")

# scootch left to make space
t.penup()
t.left(180)
t.forward(100)
t.left(180)
t.pendown()

# draw line
t.forward(150)
t.left(90)

# draw fin - turn left
for i in range(20):
    t.left(2)
    t.forward(5)

t.right(150)

# draw fin - turn right
for i in range(25):
    t.right(2)
    t.forward(5)

# draw straight line for head
t.left(70)
t.forward(150)

t.right(120)

# draw lower body
angle = 2
dist = 10
for i in range(20):
    t.right(angle)
    t.forward(dist)

# draw transparent for bottom fin later
t.penup()
for i in range(10):
    t.right(angle)
    t.forward(dist)

# bottom part of shark after bottom fin
t.pendown()
angle = 3
for i in range(15):
    t.right(angle)
    t.forward(dist)

# lower tail
t.left(105)
angle = 10
for i in range(5):
    t.right(angle)
    t.forward(10)

t.right(105)
angle = 5
for i in range(5):
    t.right(angle)
    t.forward(10)

# upper tail
t.left(90)
angle = 1
for i in range(20):
    t.right(angle)
    t.forward(10)

t.right(130)
angle = 2
for i in range(21):
    t.right(angle)
    t.forward(10)

t.left(38)
t.forward(20)

# re-position to move cursor to draw lower fin
t.penup()
t.forward(100)
t.right(85)
t.forward(120)

# draw lower fin
t.pendown()
angle = 4
for i in range(10):
    t.right(angle)
    t.forward(10)

t.left(150)
angle = 2
for i in range(17):
    t.left(angle)
    t.forward(10)

# move cursor to draw mouth
t.penup()
t.left(35)
t.forward(20)
t.right(90)
t.forward(50)

# draw lower mouth
t.left(135)
t.pendown()
angle = 10
for i in range(5):
    t.right(angle)
    t.forward(10)

# draw upper mouth
t.right(100)
angle = 10
for i in range(5):
    t.right(angle)
    t.forward(10)

t.penup()
t.left(150)
t.forward(50)

# eye
t.shape("circle")
t.stamp()

wn.exitonclick()