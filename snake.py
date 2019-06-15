import turtle
import time
import random


#Window setup
wn = turtle.Screen()
wn.title("Snake Game by Biplab")
wn.bgcolor("blue")
wn.setup(600,600)
wn.tracer(0)

#setup the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#setup the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,200)

#move the snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

#case for out of range
def inframe():
    if head.xcor()<= -300:
        head.goto(head.xcor()+600,head.ycor())
    if head.xcor()>= 300:
        head.goto(head.xcor()-600,head.ycor())
    if head.ycor()<= -300:
        head.goto(head.xcor(),head.ycor()+600)
    if head.ycor()>= 300:
        head.goto(head.xcor(),head.ycor()-600)

def addbody():
    newsegment = turtle.Turtle()
    newsegment.speed(0)
    newsegment.color("grey")
    newsegment.shape("square")
    newsegment.penup()
    newsegment.goto(0,0)
    segments.append(newsegment)
def reset():
    head.goto(0,0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000,1000)
    segments.clear()
def isaccident():
    if len(segments) != 1:
        for segment in segments:
            if segment.distance(head)<20:
                return True
    return False
def continue_segments():
    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor(),segments[i-1].ycor())
    if len(segments)>0:
        segments[0].goto(head.xcor(),head.ycor())

#Scoring System
score=0
high_score=0
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score: 0 High Score: 0", align="center",font=("Arial",24,"normal"))

segments = []
#keyboard link
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")
while True:
    wn.update()
    if head.distance(food)<20:
        food.goto(random.randint(-290,290),random.randint(-290,290))
        addbody()
        score+=1
    continue_segments()
    inframe()
    move()
    if isaccident():
        reset()
        if score>high_score:
            high_score=score
        score=0
    pen.clear()
    pen.write("Score: {} High Score: {}".format(score,high_score), align="center",font=("Arial",24,"normal"))
    time.sleep(0.1)
wn.mainloop()