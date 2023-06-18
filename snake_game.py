from turtle import Screen, Turtle
from time import sleep


def make_turtle(turtle_shape, turtle_color):
    my_turtle = Turtle()
    my_turtle.shape(turtle_shape)
    my_turtle.color(turtle_color)
    my_turtle.penup()
    my_turtle.speed('fastest')
    return my_turtle


def move():
    if snake_head.direction == "up":
        ypos = snake_head.ycor()
        snake_head.sety(ypos + 20)
    if snake_head.direction == "down":
        ypos = snake_head.ycor()
        snake_head.sety(ypos - 20)

    if snake_head.direction == "right":
        xpos = snake_head.xcor()
        snake_head.setx(xpos + 20)
    if snake_head.direction == "left":
        xpos = snake_head.xcor()
        snake_head.setx(xpos - 20)


main_surface = Screen()
main_surface.bgcolor('black')
main_surface.setup(width=600, height=600)
main_surface.title("Snake Game")

snake_head = make_turtle("square", "blue")
snake_head.goto(0, 100)
snake_head.direction = "stop"
food = make_turtle("circle", "red")

def go_up():
    snake_head.direction = "up"
def go_left():
    snake_head.direction = "left"
def go_right():
    snake_head.direction = "right"
def go_down():
    snake_head.direction = "down"

main_surface.listen()
main_surface.onkeypress(go_up,"Up")
main_surface.onkeypress(go_down,"Down")
main_surface.onkeypress(go_right,"Right")
main_surface.onkeypress(go_left,"Left")

running = True
while running == True:
    main_surface.update()
    move()
    sleep(0.2)
