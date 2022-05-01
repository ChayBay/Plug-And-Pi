import turtle
import time
import random
import sys

def load(user):
    f = open("playerSaves/"+user + "_snake.txt", "r")
    for x in f:
        hs = x
        break
    f.close()
    try:
        return hs
    except:
        return 0

def save(user, hs):
    f = open("playerSaves/"+user + "_snake.txt", "w")
    f.write(str(hs))
    f.close()

def startGame(user,hs):
    delay = 0.1

    score = 0
    high_score = int(hs)
    curr_user = user

    wn = turtle.Screen()
    wn.title("Snake Game by The Boys")
    wn.bgcolor("black")
    wn.setup(width=800, height=800)
    wn.tracer(0)

    #defining head food and additionals segments
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0,0)
    head.direction = "stop" 

    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0,100)

    segments = []

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("White")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(str(user)+"'s High Score: {}\n\n\t Score: {}".format(high_score, score), align="center", font=("Courier", 24, "normal"))

    # methods for directions
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
    def exit():
        quit()


    def move():       
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(exit, "e")
    wn.onkeypress(exit, "q")


    while True:

        wn.update()    

        #out of bounds
        if head.xcor()>390 or head.xcor()<-390 or head.ycor()>390 or head.ycor()<-390:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            score = 0

            delay = 0.1

            pen.clear()
            pen.write(str(user)+"'s High Score: {}\n\n\t Score: {}".format(high_score, score), align="center", font=("Courier", 24, "normal"))

        #getting food
        if head.distance(food) < 20:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            segments.append(new_segment)

            #delay -= 0.01

            score += 10

            if score > high_score:
                high_score = score
                save(user, high_score)
            
            pen.clear()
            pen.write(str(user)+"'s High Score: {}\n\n\t Score: {}".format(high_score, score), align="center", font=("Courier", 24, "normal"))


        #moving body
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x,y)


        move()


        #colliding with itself
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0,0)
                head.direction = "stop"

                for segment in segments:
                    segment.goto(1000,1000)

                segments.clear()

                score = 0

                delay = 0.1

                pen.clear()
                pen.write(str(user) +" 's Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
            

        time.sleep(delay)

   


def main(args,user):
    if args == 1:
        wn = turtle.Screen()
        hs = load(user)
        startGame(user,hs)
        wn.exitonclick()

        

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main(1,"Chason")
