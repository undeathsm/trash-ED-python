from graph import *
import math

windowSize(480, 480)
width, height = windowSize()

def paint_cloud(x_start, y_start, n = 7):
    x = x_start
    r = 18
    penColor("grey")
    brushColor("white")
    for i in range(n):
        if i % 2 == 0:
            circle(x, y_start, r)
        else:
            circle(x, y_start-r, r)

        x += r / 1.5

penColor("skyblue")
brushColor("skyblue")
rectangle(0, 0, width, height * 0.4)
penColor("blue")
brushColor("blue")
rectangle(0, height * 0.4, width, height * 0.65)
penColor("yellow")
brushColor("yellow")
rectangle(0, height * 0.65, width, height)

paint_cloud(100, 100)

penColor("yellow")
brushColor("yellow")
r = 40
l = 40
circle(width - l - r, l + r + 10, r)

run()