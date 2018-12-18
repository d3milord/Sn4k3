import turtle
import time
import random


delay = 0.2
movement = 20
window_size_x = 600
window_size_y = 600
scale = 20

tail = []


def window_setup():
    wn.title("Sn4k3")
    wn.bgcolor("green")
    wn.setup(width=window_size_x, height=window_size_y)


def head_setup():
    head.speed(0)
    head.shape("square")
    head.color("grey")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"


def food_setup():
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)


def init():
    window_setup()
    head_setup()
    food_setup()


def move():
    if len(tail) > 0:
        tail[0].setx(head.xcor())
        tail[0].sety(head.ycor())
        for _tail_number in range(1, len(tail)-1):
            tail[_tail_number].setx(tail[_tail_number - 1].xcor())
            tail[_tail_number].sety(tail[_tail_number - 1].ycor())
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + movement)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - movement)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + movement)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - movement)
    head.direction = "stop"


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def key_mapping():
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(go_left, "a")


def move_random_food():
    while True:
        x = random.randrange(-280, +280, 20)
        y = random.randrange(-280, +280, 20)
        if not new_food_spot_matches_snake(x, y):
            food.goto(x, y)
            break


def new_food_spot_matches_snake(x, y):
    if head.ycor() == y and head.xcor() == x:
        return True
    return False


def head_food_collision():
    if head.ycor() == food.ycor() and head.xcor() == food.xcor():
        return True
    return False


def snake_add_tail():
    new_tail = turtle.Turtle()
    new_tail.speed(0)
    new_tail.shape("square")
    new_tail.color("grey")
    new_tail.penup()
    new_tail.goto(food.xcor(), food.ycor())
    new_tail.direction = "stop"
    tail.append(new_tail)


wn = turtle.Screen()
head = turtle.Turtle()
food = turtle.Turtle()

init()
key_mapping()
wn.tracer(0)


while True:
    wn.update()
    move()
    time.sleep(delay)
    if head_food_collision():
        snake_add_tail()
        move_random_food()


wn.mainloop()
