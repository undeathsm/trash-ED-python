from graph import *
import math

canvasSize(430, 610)
windowSize(430, 610)
width, height = windowSize()

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

    #body
    penColor("")
    brushColor("#6C6753")

    body = [
        {"x0": 10, "y0": 130, "width": 40, "height": 12},
        {"x0": 17, "y0": 90, "width": 35, "height": 80},
        {"x0": 70, "y0": 140, "width": 40, "height": 12},
        {"x0": 77, "y0": 100, "width": 35, "height": 80},
        {"x0": 70, "y0": 60, "width": 120, "height": 60},
        {"x0": 155, "y0": 70, "width": 30, "height": 40},
        {"x0": 155, "y0": 123, "width": 30, "height": 10},
        {"x0": 165, "y0": 100, "width": 12, "height": 40},
        {"x0": 112, "y0": 60, "width": 50, "height": 50},
        {"x0": 112, "y0": 103, "width": 30, "height": 10},
        {"x0": 122, "y0": 80, "width": 12, "height": 40},
        {"x0": 135, "y0": 55, "width": 60, "height": 40},
    ]

    for part_of_body in body:
        ellipse(
            x0 + part_of_body["x0"]*s*r,
            y0 + part_of_body["y0"]*s,
            part_of_body["width"]*s,
            part_of_body["height"]*s
        )
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

def paint_chain(x0, y0, xl, yl):
    r = 10
    n = (((xl - x0) / (r * 0.7))**2)**0.5
    dx = (xl - x0) / n
    dy = (yl - y0) / n
    x = x0 + dx
    y = y0 + dy
    penColor("black")
    brushColor("")
    for i in range(int(math.ceil(n))):
        if i % 2 == 0:
            ellipse(x, y, r, 1.2*r)
        else:
            ellipse(x, y, 1.2*r, r)

        x += dx
        y += dy

#background
penColor("")
brushColor("#5FBCD3")
rectangle(0, 0, width, height * 0.4)
brushColor("#37C871")
rectangle(0, height * 0.4, width, height)
#walls
paint_wall(80, 12, 1.4)
paint_wall(-60, 120, 0.9)
paint_wall(-80, 210, 0.8)
paint_wall(200, 175, 0.85)

#dogs
paint_dog(40, 295)
paint_dog(width + 10, 290, 0.7, True)
paint_dog(220, 450, 1, True)
#chain
paint_chain(200, 450, 300, 350)
paint_chain(200, 450, 220, 450)
paint_chain(210, 420, 220, 450)
#dog house
s = 1
r = 1
brushColor("#C8AB37")
p1 = (255*s*r, 300*s)
p2 = (255*s*r, 400*s)
p3 = (350*s*r, 420*s)
p4 = (350*s*r, 320*s)
polygon([p1, p2, p3, p4])

p1 = (350*s*r, 320*s)
p2 = (350*s*r, 420*s)
p3 = (375*s*r, 395*s)
p4 = (375*s*r, 295*s)
polygon([p1, p2, p3, p4])

brushColor("#D4AA00")
p1 = (255*s*r, 300*s)
p2 = (350*s*r, 320*s)
p3 = (310*s*r, 230*s)
polygon([p1, p2, p3])

p1 = (350*s*r, 320*s)
p2 = (310*s*r, 230*s)
p4 = (375*s*r, 295*s)
p3 = (340*s*r, 215*s)
polygon([p1, p2, p3, p4])

penColor("")
brushColor("black")
ellipse(300, 370, 50, 60)

paint_dog(250, 370, 2.5)

run()