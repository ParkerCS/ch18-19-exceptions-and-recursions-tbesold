import turtle

my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor('blue')
# Draw Here
my_turtle.fillcolor("red")

my_turtle.begin_fill()
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()

my_turtle.width(10)
my_turtle.up()
my_turtle.goto(-100, -100)
my_turtle.down()

my_turtle.setheading(135)
my_turtle.forward(100)

#my_turtle.begin_fill()
heading = 0
curl = 0.1

for i in range(50):
    my_turtle.setheading(heading)
    curl += 0.1
    heading += curl
    my_turtle.forward(5)
#my_turtle.end_fill()

my_screen.exitonclick()


