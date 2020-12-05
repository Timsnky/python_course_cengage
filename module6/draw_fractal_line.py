from turtle import Turtle


def drawFractalLine(t, distance, angle, level):
    if level == 0:
        t.up()
        t.setheading(angle)
        t.down()
        t.forward(distance)
        t.up()
    else:
        drawFractalLine(t, distance / 3, angle, level - 1)
        drawFractalLine(t, distance / 3, angle + 60, level - 1)
        drawFractalLine(t, distance / 3, angle - 60, level - 1)
        drawFractalLine(t, distance / 3, angle, level - 1)


def main():
    t = Turtle()
    drawFractalLine(t, 200, 0, 4)
    drawFractalLine(t, 200, -120, 4)
    drawFractalLine(t, 200, 120, 4)


if __name__ == "__main__":
    main()





