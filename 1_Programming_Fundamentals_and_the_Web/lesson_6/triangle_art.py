import turtle
def draw_triangle(some_turtle):
    some_turtle.forward(100)
    for i in range(1,3):
        some_turtle.right(120)
        some_turtle.forward(100)

def draw_second_triangle(some_turtle):
    some_turtle.forward(200)
    for i in range(1,3):
        some_turtle.right(120)
        some_turtle.forward(200)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    # initiate turtle
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(50)
    for i in range(1,90):
        draw_triangle(some_turtle=brad)
        brad.left(4)
    for i in range(1,24):
        draw_second_triangle(brad)
        brad.left(15)
        brad.forward(300)
    window.exitonclick()
draw_art()