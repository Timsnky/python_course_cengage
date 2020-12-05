from turtle import Turtle
import math


def drawCircle(t, x, y, radius):
    t.up()
    t.goto(x, y)
    t.setheading(0)
    t.forward(radius)
    t.setheading(90)
    t.down()

    movement_distance = (2 * math.pi * radius) / 120

    for position in range(120):
        t.left(3)
        t.forward(movement_distance)


def main():
    t = Turtle()
    drawCircle(t, 50, 75, 100)


if __name__ == "__main__":
    main()