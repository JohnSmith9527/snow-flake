import turtle,random

x=0
y=0
turtle.colormode(255)


for i in range(12):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    r=random.randint(200,255)
    g=random.randint(150,200)
    b=random.randint(20,100)
    turtle.pencolor(r,g,b)
    for j in range(2):
        turtle.forward(100)
        turtle.dot(50)
    turtle.left(30)