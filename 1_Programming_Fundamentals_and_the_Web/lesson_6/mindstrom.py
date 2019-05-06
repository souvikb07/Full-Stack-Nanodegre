import turtle
def draw_square(some_turtle):
    for j in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    # make window screen
    window = turtle.Screen()
    window.bgcolor('pink')
    # create personalize turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color('green')
    brad.speed(2)
    draw_square(brad)
    # draw circle
    angie = turtle.Turtle()
    angie.color('blue')
    angie.shape('classic')
    angie.circle(100)
    # draw triangle
    trian = turtle.Turtle()
    trian.shape('triangle')
    trian.forward(100)
    trian.right(90)
    trian.forward(100)
    trian.right(60)
    trian.forward(100)
    trian.left(120)
    trian.forward(100)
    trian.left(120)
    trian.forward(100)
    #exit the window
    window.exitonclick()
draw_art()