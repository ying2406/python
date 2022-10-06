import turtle
turtle.setup

def driehoek():
    
    turtle.color("pink")

for x in range(3):
    
    turtle.color("pink")
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100) 

    turtle.penup()
    turtle.right(150)
    turtle.forward(50)

    turtle.color("blue")
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(120)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(100)

    turtle.left(120)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(100)
    turtle.left(90)
    turtle.left(90)
    turtle.left(30)
    turtle.left(30)
    turtle.forward(100)


driehoek() 
input()