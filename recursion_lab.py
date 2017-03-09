'''
Using the turtle library, create a fractal pattern.
You may use heading/forward/backward or goto and fill commands to draw
your fractal.  Ideas for your fractal pattern might include
examples from the chapter.  You can find many fractal examples online,
but please make your fractal unique.  Experiment with the variables
to change the appearance and behavior.

Give your fractal a depth of at least 5.  Ensure the fractal is contained on the screen (at whatever size you set it).  Have fun.
(35pts)
'''

import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

color_list = ["gold", "blue"]


def draw(x, y, heading, distance, depth):
    #my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.color(color_list[depth % len(color_list)])
    my_turtle.fillcolor(color_list[depth % len(color_list)])
    #my_turtle.down()
    my_turtle.setheading(heading)
    my_turtle.forward(distance)

    new_y = my_turtle.ycor() #+ 4
    new_x = my_turtle.xcor() #- 4

    if depth > 0:
        draw(new_x, new_y, heading + 5, distance / 1.7, depth - 1)
        draw(new_x, new_y, heading - 5, distance / 1.7, depth - 1)


my_turtle.speed(0)
my_turtle.width(3)

for i in range(0, 360, 15):
    draw(0, 0, i, 70, 5)
my_screen.exitonclick()