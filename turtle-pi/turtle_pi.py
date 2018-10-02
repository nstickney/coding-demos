"""
Visualize calculating pi with random numbers using the turtle
"""

__author__ = "nstickney"
__version__ = "0.1.0"
__license__ = "AGPLv2.1"

import math
import random
import sys
import turtle


def calculate_pi(d, r, s, t, v):
    """ Calculates pi with random numbers and draws a turtle visualization """
    # random.seed("TOTALLY RANDOM")
    if v:
        t.shape("circle")
        t.up()
        t.goto(0, - r)
        t.down()
        t.circle(r)
        t.up()

    hits = 0

    for i in range(1, d + 1):
        x = random.random() * (2 * r) - r
        y = random.random() * (2 * r) - r
        if (x ** 2 + y ** 2 <= r ** 2):
            if v:
                t.color("green")
            hits += 1
        else:
            if v:
                t.color("red")
        if v:
            t.goto(x, y)
            t.dot(r/75)
        if i % (d // 100) == 0:
            print(i, "dots:", " " * (max(len(str(d)), 4) - len(str(i))),
                  "Pi =", hits / i * 4)
            if v:
                t.color("black")
                s.update()

    print("Reference:", " " * (max(len(str(d)), 4) - 4), "Pi =", math.pi)


def print_usage():
    """ Print a usage statement for python-turtle-pi """
    print("Usage: python[3]", sys.argv[0], "[--no-viz] <dots> [radius]")
    print("    --no-viz : don't run the visualization (increases speed)")
    print("    dots     : number of points to check")
    print("    radius   : radius of square/circle")
    sys.exit()


if __name__ == "__main__":

    if 2 > len(sys.argv) or 4 < len(sys.argv):
        print_usage()

    RADIUS = 150
    DRAW = True
    if sys.argv[1] == "--no-viz":
        DRAW = False
        DOTS = int(sys.argv[2])
        if len(sys.argv) > 3:
            RADIUS = int(sys.argv[3])
    else:
        DOTS = int(sys.argv[1])
        if len(sys.argv) > 2:
            RADIUS = int(sys.argv[2])

    PAD = None
    PEN = None

    if DRAW:
        PAD = turtle.Screen()
        PAD.tracer(0)
        PEN = turtle.Turtle()
        PEN.speed(0)

    calculate_pi(DOTS, RADIUS, PAD, PEN, DRAW)

    if DRAW:
        PAD.exitonclick()
