from graph import *
import math

canvasSize(430, 610)
windowSize(430, 610)

def ellipse(x0, y0, width, height):
    a = width / 2
    b = height / 2
    p = []

    n = int(math.ceil((2*width + 2*height) / 1))
    fi1 = 0
    fi2 = 360
    fi = fi1
    dfi = (fi2 - fi1) / n

    for i in range(n):
        x = x0 + a * math.cos(fi * math.pi / 180)
        y = y0 + b * math.sin(fi * math.pi / 180)

        fi += dfi
        p.append((x, y))

    polygon(p)

# penColor("black")
# brushColor("#DED599")
# paint_ellipse(215, 305, 430, 610)

def paint_wall(x0, y0, scale = 1, reverse = False):
    r = 1
    if reverse:
        r = -1

    s = scale
    width = 25
    height = 200
    desks_width = [
        width * 1.1,
        width * 0.9,
        width,
        width * 1.2,
        width * 0.9,
        width * 1.05,
        width * 1.1,
        width,
        width * 0.95,
        width * 1.1,
        width * 1.05,
        width * 0.9,
        width
    ]

    x = x0
    y = y0
    penColor("black")
    brushColor("#C8AB37")
    for width in desks_width:
        rectangle(x, y, x + width*s*r, y + height*s)
        x += width * s * r

    penColor("grey")
    brushColor("")
    rectangle(x0, y0, x, y + height*s)

# paint_wall(100, 100)
# paint_wall(75, 150, 1.5, True)
def mouth(x0, y0, scale = 1, r = 1):
    s = scale

    n = 100
    p = []
    a = 0
    for i in range(n):
        b = (1.85 - a/10)**4 / 1.2
        p.append((x0 + a*s*r, y0 + b*s))
        a += 20 / n

    a = 0
    for i in range(n):
        b = (a/10)**4 / 1.5
        p.append((x0 + a*s*r + 20*r*s, y0 + b*s))
        a += 20 / n

    penColor("black")
    polyline(p)

def paint_dog(x0, y0, scale = 1, reverse = False):
    r = 1
    if reverse:
        r = -1

    s = scale

    #head
    penColor("black")
    penSize("2")
    brushColor("#6C6753")
    rectangle(x0 + 10*s*r, y0 + 10*s, x0 + 75*s*r, y0 + 75*s)
    penSize("1")
    ellipse(x0 + 10*s*r, y0 + 24*s, 20*s*r, 25*s)
    ellipse(x0 + 72*s*r, y0 + 23*s, 20*s*r, 25*s)
    #head eyes
    brushColor("white")
    ellipse(x0 + 27*s*r, y0 + 37*s, 15*s, 5*s)
    ellipse(x0 + 53*s*r, y0 + 37*s, 15*s, 5*s)
    brushColor("black")
    circle(x0 + 27*s*r, y0 + 37*s, 2.5*s)
    circle(x0 + 53*s*r, y0 + 37*s, 2.5*s)
    #head mouth
    mouth(x0 + 20*s*r, y0 + 55*s, 1*s, r)
    brushColor("white")
    p1 = (x0 + 22*s*r, y0 + 61*s)
    p2 = (x0 + 23.5*s*r, y0 + 50*s)
    p3 = (x0 + 27*s*r, y0 + 56*s)
    polygon([p1, p2, p3])
    p1 = (x0 + 57*s*r, y0 + 61*s)
    p2 = (x0 + 55*s*r, y0 + 50*s)
    p3 = (x0 + 52*s*r, y0 + 56*s)
    polygon([p1, p2, p3])

    #body
    

paint_dog(200, 200, 2)

run()