from graph import *
import math

windowSize(800, 480)
canvasSize(800, 480)
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

def paint_sector(fi1, fi2, x0, y0, r, scale_x = 1, scale_y = 1):
    fi = fi1
    n = 100
    dfi = (fi1 - fi2) / n
    points = [(x0, y0)]

    for i in range(n):
        x = x0 + r*scale_x*math.cos(math.pi*fi / 180)
        y = y0 + r*scale_y*math.sin(math.pi*fi / 180)
        p = (x, y)
        points.append(p)

        fi += dfi

    polygon(points)

def paint_sun(x0, y0, r1, r2, scale_x = 1, scale_y = 1):
    a1 = r1 * scale_x
    b1 = r1 * scale_y
    a2 = r2 * scale_x
    b2 = r2 * scale_y
    p = []

    n = 90
    fi1 = 0
    fi2 = 360
    fi = fi1
    dfi = (fi2 - fi1) / n

    for i in range(n):
        if i % 2 == 0:  
            x = x0 + a1 * math.cos(fi * math.pi / 180)
            y = y0 + b1 * math.sin(fi * math.pi / 180)
        else:
            x = x0 + a2 * math.cos(fi * math.pi / 180)
            y = y0 + b2 * math.sin(fi * math.pi / 180)

        fi += dfi
        p.append((x, y))

    polygon(p)

def paint_cloud(x_start, y_start, scale_x = 1, scale_y = 1, n = 7):
    dx = 0
    r = 18
    el_width = 2*r*scale_x
    el_height = 2*r*scale_y
    penColor("grey")
    brushColor("white")
    for i in range(n):
        x = x_start + dx*scale_x

        if i % 2 == 0:
            y = y_start
            ellipse(x, y, el_width, el_height)
        else:
            y = y_start - r*scale_y
            ellipse(x, y, el_width, el_height)

        dx += r / 1.5

def paint_waves(x0, y0, r, dy):
    length = 2 * (r**2 - dy**2)**0.5
    if r <= dy:
        length = r
    n = int(math.ceil((width - x0) / length)) + 1

    for i in range(n):
        if i % 2 == 0:
            penColor("#4423DF")
            brushColor("#4423DF")
            circle(x0 + length * i, y0 - dy, r)
        else:
            penColor("yellow")
            brushColor("yellow")
            circle(x0 + length * i, y0 + dy, r)

def paint_umbrella(x0, y0, scale_x = 1, scale_y = 1):
    penColor("orange")
    brushColor("orange")
    rectangle(x0 + 90*scale_x, y0 + 220*scale_y, x0 + 100*scale_x, y0 + 40*scale_y)
    penColor("purple")
    brushColor("#F45151")
    rectangle(x0 + 90*scale_x, y0 + 40*scale_y, x0 + 100*scale_x, y0)

    start = x0
    end = x0 + 90*scale_x
    length = end - start
    n = 4
    for i in range(n):
        p1 = (x0 + 90*scale_x, y0)
        p2 = (start + (length / n) * i, y0 + 40*scale_y)
        p3 = (start + (length / n) * (i + 1), y0 + 40*scale_y)
        polygon([p1, p2, p3])

    start = x0 + 190*scale_x
    end = x0 + 100*scale_x
    length = end - start
    n = 4
    for i in range(n):
        p1 = (x0 + 100*scale_x, y0)
        p2 = (start + (length / n) * i, y0 + 40*scale_y)
        p3 = (start + (length / n) * (i + 1), y0 + 40*scale_y)
        polygon([p1, p2, p3])

def paint_ship(x0, y0, scale_x = 1, scale_y = 1):
    penColor("#BA5005")
    brushColor("#BA5005")
    rectangle(x0, y0 + 30*scale_y, x0 + 150*scale_x, y0 + 60*scale_y)
    penColor("black")
    brushColor("black")
    rectangle(x0 + 72*scale_x, y0 - 80*scale_y, x0 + 78*scale_x, y0 + 30*scale_y)

    penColor("#BA5005")
    brushColor("#BA5005")
    paint_sector(-180, -90, x0, y0 + 30*scale_y, 30, 0.7*scale_x, scale_y)

    paint_sector(0, -90, x0 + 150*scale_x, y0 + 30*scale_y, 30, (7/3)*scale_x, scale_y)

    penColor("black")
    brushColor("black")
    ellipse(x0 + 180*scale_x, y0 + 42*scale_y, 18*scale_x, 18*scale_y)
    penColor("white")
    brushColor("white")
    ellipse(x0 + 180*scale_x, y0 + 42*scale_y, 12*scale_x, 12*scale_y)

    penColor("black")
    brushColor("#DED599")
    p1 = (x0 + 77*scale_x, y0 - 80*scale_y)
    p2 = (x0 + 102*scale_x, y0 - 25*scale_y)
    p3 = (x0 + 147*scale_x, y0 - 25*scale_y)
    polygon([p1, p2, p3])

    p1 = (x0 + 77*scale_x, y0 + 30*scale_y)
    polygon([p1, p2, p3])

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
paint_waves(-10, height * 0.65, 40, 32)

# sun
penColor("yellow")
brushColor("yellow")
paint_sun(width - 100, 100, 40, 55)

# cloud
paint_cloud(200, 50)
paint_cloud(120, 130, 1.3, 1.3, 5)
paint_cloud(325, 90, 1.6, 1.6, 7)

# ships
paint_ship(480, 200, 1, 1)
paint_ship(290, 190, .5, .5)

# umbrella
paint_umbrella(10, 240)
paint_umbrella(220, 300, 0.33, 0.6)


run()