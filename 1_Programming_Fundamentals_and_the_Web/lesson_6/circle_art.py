import turtle
def draw_square(some_turtle):
    for j in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
def draw_art():
    window = turtle.Screen()
    window.bgcolor('pink')
    # create personalize turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('green')
    brad.speed(50)
    for i in range(1,180):
        draw_square(brad)
        brad.left(2)
    window.exitonclick()
draw_art()