import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(0, 2):
    t.pencolor('lime')
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.left(90)
    
t.penup()
t.forward(200)
t.pendown()
for l in range(0,2):
    t.pencolor('blue')
    t.forward(40)
    t.left(90)
    t.forward(80)
    t.left(90)
