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

# background
penColor("#A1F5FF")
brushColor("#A1F5FF")
rectangle(0, 0, width, height * 0.4)
penColor("#4423DF")
brushColor("#4423DF")
rectangle(0, height * 0.4, width, height * 0.65)
penColor("yellow")
brushColor("yellow")
rectangle(0, height * 0.65, width, height)

# cloud
paint_cloud(100, 100)

# sun
penColor("yellow")
brushColor("yellow")
r = 40
l = 40
circle(width - l - r, l + r + 10, r)

# umbrella
penColor("orange")
brushColor("orange")
rectangle(100, height - 20, 110, height - 200)
penColor("purple")
brushColor("#F45151")
rectangle(100, height - 200, 110, height - 240)

start = 10
end = 100
length = end - start
n = 4
for i in range(n):
    p1 = (100, height - 240)
    p2 = (start + (length / n) * i, height - 200)
    p3 = (start + (length / n) * (i + 1), height - 200)
    polygon([p1, p2, p3])

start = 200
end = 110
length = end - start
n = 4
for i in range(n):
    p1 = (110, height - 240)
    p2 = (start + (length / n) * i, height - 200)
    p3 = (start + (length / n) * (i + 1), height - 200)
    polygon([p1, p2, p3])

# ship
def paint_sector(fi1, fi2, x0, y0, r):
    fi = fi1
    n = 100
    dfi = (fi1 - fi2) / n
    p3 = (x0, y0)

    for i in range(n):
        x = x0 + r * math.cos(math.pi*fi / 180)
        y = y0 + r * math.sin(math.pi*fi / 180)
        p1 = (x, y)

        x = x0 + r * math.cos(math.pi*(fi + dfi) / 180)
        y = y0 + r * math.sin(math.pi*(fi + dfi) / 180)
        p2 = (x, y)

        polygon([p1, p2, p3])

        fi += dfi

penColor("#BA5005")
brushColor("#BA5005")
rectangle(240, height * 0.4 + 30, 390, height * 0.4 + 60)
penColor("black")
brushColor("black")
rectangle(312, height * 0.4 - 80, 318, height * 0.4 + 30)

penColor("#BA5005")
brushColor("#BA5005")
paint_sector(-180, -90, 240, height * 0.4 + 30, 30)

p1 = (390, height * 0.4 + 60)
p2 = (390, height * 0.4 + 30)
p3 = (460, height * 0.4 + 30)
polygon([p1, p2, p3])

penColor("black")
brushColor("black")
circle(405, height * 0.4 + 41, 9)
penColor("white")
brushColor("white")
circle(405, height * 0.4 + 41, 6)

# 312, height * 0.4 - 80, 318, height * 0.4 + 30
penColor("black")
brushColor("#DED599")
p1 = (317, height * 0.4 - 80)
p2 = (342, height * 0.4 - 25)
p3 = (387, height * 0.4 - 25)
polygon([p1, p2, p3])

p1 = (317, height * 0.4 + 30)
polygon([p1, p2, p3])


run()