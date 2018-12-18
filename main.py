import turtle
import time
import random


delay = 0.2
movement = 20
window_size_x = 600
window_size_y = 600
scale = 20

tail = []

life = 5
score = 0


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


def board_setup():
    board.speed(0)
    board.shape("square")
    board.color("white")
    board.penup()
    board.hideturtle()
    board.goto(0, 260)
    update_board()

def init():
    window_setup()
    head_setup()
    food_setup()
    board_setup()


def move_head():
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


def move_body():
    for index in range(len(tail) - 1, 0, -1):
        x = tail[index - 1].xcor()
        y = tail[index - 1].ycor()
        tail[index].goto(x, y)

    if len(tail) > 0:
        x = head.xcor()
        y = head.ycor()
        tail[0].goto(x, y)


def move():
    move_body()
    move_head()


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
    return new_food_spot_matches_head(x, y) or new_food_spot_matches_tail(x, y)


def new_food_spot_matches_tail(x, y):
    for index in range(0, len(tail)):
        if tail[index].ycor() == y and tail[index].xcor() == x:
            return True
    return False


def new_food_spot_matches_head(x, y):
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
    new_tail.goto(head.xcor(), head.ycor())
    tail.append(new_tail)


def lose_life():
    global life
    life -= 1


def reset_snake():
    global tail
    for tail_piece in tail:
        tail_piece.ht()
    tail = []
    head.goto(0, 0)
    head.direction = "stop"


def border_collision():
    if head.xcor() < -280 or head.xcor() > 280 or head.ycor() < -280 or head.ycor() > 280:
        return True
    return False


def snake_collision():
    for tail_piece in tail:
        if tail_piece.xcor() == head.xcor() or tail_piece.ycor() == head.ycor():
            return True
    return False


def end_game():
    print("end game")


def increase_score():
    global score
    score += 1


def increase_difficulty():
    global delay
    delay += 0.01


def update_board():
    board.clear()
    board.write("Score: {}  Lifes: {}".format(score, life), align="center", font=("Courier", 24, "normal"))


wn = turtle.Screen()
head = turtle.Turtle()
food = turtle.Turtle()
board = turtle.Turtle()

init()
key_mapping()
wn.tracer(0)


while True:
    wn.update()
    move()
    update_board()
    time.sleep(delay)
    if head_food_collision():
        snake_add_tail()
        move_random_food()
        increase_score()
        print("score: " + str(score))
    if border_collision() or snake_collision():
        lose_life()
        reset_snake()
        print("lost a life")
        print("lifes: " + str(life))
    if life < 0:
        end_game()
        break


wn.mainloop()
