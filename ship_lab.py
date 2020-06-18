from graph import *
from time import monotonic
import math
import random

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

    return polygon(p)

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

    return polygon(points)

def paint_cloud(x_start, y_start, scale_x = 1, scale_y = 1, n = 7):
    dx = 0
    r = 18
    el_width = 2*r*scale_x
    el_height = 2*r*scale_y
    penColor("grey")
    brushColor("white")
    cloud = []
    for i in range(n):
        x = x_start + dx*scale_x

        if i % 2 == 0:
            y = y_start
            cloud.append(circle(x, y, el_width / 2))
        else:
            y = y_start - r*scale_y
            cloud.append(circle(x, y, el_width / 2))

        dx += r / 1.5

    return cloud

class Background():
    sky = {}
    water = {}
    sand = {}
    waves = []
    x0 = -100
    x = x0
    y0 = height * 0.65
    period = 2500
    r = 40
    dy = 32

    def paint_background(self):
        if self.sky is not {}:
            deleteObject(self.sky)

        if self.water is not {}:
            deleteObject(self.water)

        if self.sand is not {}:
            deleteObject(self.sand)

        penColor("#A1F5FF")
        brushColor("#A1F5FF")
        self.sky = rectangle(0, 0, width, height * 0.4)

        penColor("#4423DF")
        brushColor("#4423DF")
        self.water = rectangle(0, height * 0.4, width, height * 0.65)

        penColor("yellow")
        brushColor("yellow")
        self.sand = rectangle(0, height * 0.65, width, height)

        self.paint_waves()

        self.next_step()

    def paint_waves(self):
        for obj in self.waves:
            deleteObject(obj)

        self.waves = []
        
        length = 2 * (self.r**2 - self.dy**2)**0.5
        if self.r <= self.dy:
            length = self.r
        n = int(math.ceil((width - self.x) / length)) + 1

        for i in range(n):
            if i % 2 == 0:
                penColor("#4423DF")
                brushColor("#4423DF")
                self.waves.append(circle(self.x + length * i, self.y0 - self.dy, self.r))
            else:
                penColor("yellow")
                brushColor("yellow")
                self.waves.append(circle(self.x + length * i, self.y0 + self.dy, self.r))
                
    def next_step(self):
        length = 2 * (self.r**2 - self.dy**2)**0.5
        if self.x >= 2*length + self.x0:
            self.x = self.x0
        else:
            self.x += length * (15 / self.period)
        

class Sun:
    x0 = width - 100
    y0 = 100
    r1 = 40
    r2 = 55
    r2_const = 55
    dr2 = 5
    period = 2000
    fi = 0
    scale_x = 1
    scale_y = 1
    obj = {}

    def paint_sun(self):
        if self.obj is not {}:
            deleteObject(self.obj)

        penColor("")
        brushColor("yellow")
        a1 = self.r1 * self.scale_x
        b1 = self.r1 * self.scale_y
        a2 = self.r2 * self.scale_x
        b2 = self.r2 * self.scale_y
        p = []

        n = 90
        fi1 = 0
        fi2 = 360
        fi = fi1
        dfi = (fi2 - fi1) / n

        for i in range(n):
            if i % 2 == 0:  
                x = self.x0 + a1 * math.cos(fi * math.pi / 180)
                y = self.y0 + b1 * math.sin(fi * math.pi / 180)
            else:
                x = self.x0 + a2 * math.cos(fi * math.pi / 180)
                y = self.y0 + b2 * math.sin(fi * math.pi / 180)

            fi += dfi
            p.append((x, y))

        self.obj = polygon(p)
        self.next_step()
    
    def next_step(self):
        self.r2 = self.r2_const + self.dr2*math.sin(self.fi)
        if self.fi > 2*math.pi: self.fi = 0
        self.fi = self.fi + (15 / self.period)*2*math.pi

class Clouds():
    clouds = []
    cloud_1 = {
        "x0": 200,
        "y0": 50
    }

    cloud_2 = {
        "x0": 120,
        "y0": 130,
        "scale_x": 1.3,
        "scale_y": 1.3,
        "n": 5
    }

    cloud_3 = {
        "x0": 325,
        "y0": 90,
        "scale_x": 1.6,
        "scale_y": 1.6,
        "n": 7
    }

    period = 1000000


    def paint_clouds(self):
        for cloud in self.clouds:
            for ellipse in cloud:
                deleteObject(ellipse)

        self.clouds.append(
            paint_cloud(
                self.cloud_1["x0"],
                self.cloud_1["y0"]
            )
        )

        self.clouds.append(
            paint_cloud(
                self.cloud_2["x0"],
                self.cloud_2["y0"],
                self.cloud_2["scale_x"],
                self.cloud_2["scale_y"],
                self.cloud_2["n"],
            )
        )

        self.clouds.append(
            paint_cloud(
                self.cloud_3["x0"],
                self.cloud_3["y0"],
                self.cloud_3["scale_x"],
                self.cloud_3["scale_y"],
                self.cloud_3["n"],
            )
        )

        self.next_step()

    def next_step(self):
        if (self.cloud_1["x0"] > width + 500):
            self.cloud_1["x0"] -= width + 500
            self.cloud_2["x0"] -= width + 500
            self.cloud_3["x0"] -= width + 500
            return

        dx =  (width + 200) * 15 / self.period
        self.cloud_1["x0"] = self.cloud_1["x0"] + dx
        self.cloud_2["x0"] = self.cloud_2["x0"] + dx
        self.cloud_3["x0"] = self.cloud_3["x0"] + dx

class Ship():
    def __init__(self, x0, y0, scale_x = 1, scale_y = 1, period = 50000):
        self.x0 = x0
        self.y0 = y0
        self.period = period
        self.scale_x = scale_x
        self.scale_y = scale_y

    objects = []

    def paint_ship(self):
        x0 = self.x0
        y0 = self.y0
        scale_x = self.scale_x
        scale_y = self.scale_y

        #zeoring self.objects
        for obj in self.objects:
            deleteObject(obj)
        self.objects = []

        penColor("#BA5005")
        brushColor("#BA5005")
        obj = rectangle(x0, y0 + 30*scale_y, x0 + 150*scale_x, y0 + 60*scale_y)
        self.objects.append(obj)
        penColor("black")
        brushColor("black")
        obj = rectangle(x0 + 72*scale_x, y0 - 80*scale_y, x0 + 78*scale_x, y0 + 30*scale_y)
        self.objects.append(obj)

        penColor("#BA5005")
        brushColor("#BA5005")
        paint_sector(-180, -90, x0, y0 + 30*scale_y, 30, 0.7*scale_x, scale_y)

        paint_sector(0, -90, x0 + 150*scale_x, y0 + 30*scale_y, 30, (7/3)*scale_x, scale_y)

        penColor("black")
        brushColor("black")
        obj = ellipse(x0 + 180*scale_x, y0 + 42*scale_y, 18*scale_x, 18*scale_y)
        self.objects.append(obj)
        penColor("white")
        brushColor("white")
        obj = ellipse(x0 + 180*scale_x, y0 + 42*scale_y, 12*scale_x, 12*scale_y)
        self.objects.append(obj)

        penColor("black")
        brushColor("#DED599")
        p1 = (x0 + 77*scale_x, y0 - 80*scale_y)
        p2 = (x0 + 102*scale_x, y0 - 25*scale_y)
        p3 = (x0 + 147*scale_x, y0 - 25*scale_y)
        obj = polygon([p1, p2, p3])
        self.objects.append(obj)

        p1 = (x0 + 77*scale_x, y0 + 30*scale_y)
        obj = polygon([p1, p2, p3])
        self.objects.append(obj)
        
        self.next_step()

    def next_step(self):
        pass

class Umbrella():
    def __init__(self, x0, y0, scale_x=1, scale_y=1):
        self.x0 = x0
        self.y0 = y0
        self.scale_x = scale_x
        self.scale_y = scale_y

    objects = []

    def paint_umbrella(self):
        x0 = self.x0
        y0 = self.y0
        scale_x = self.scale_x
        scale_y = self.scale_y

        #zeoring self.objects
        for obj in self.objects:
            deleteObject(obj)
        self.objects = []
        
        penColor("orange")
        brushColor("orange")
        obj = rectangle(x0 + 90*scale_x, y0 + 220*scale_y, x0 + 100*scale_x, y0 + 40*scale_y)
        self.objects.append(obj)
        penColor("purple")
        brushColor("#F45151")
        obj = rectangle(x0 + 90*scale_x, y0 + 40*scale_y, x0 + 100*scale_x, y0)
        self.objects.append(obj)

        start = x0
        end = x0 + 90*scale_x
        length = end - start
        n = 4
        for i in range(n):
            p1 = (x0 + 90*scale_x, y0)
            p2 = (start + (length / n) * i, y0 + 40*scale_y)
            p3 = (start + (length / n) * (i + 1), y0 + 40*scale_y)
            obj = polygon([p1, p2, p3])
            self.objects.append(obj)

        start = x0 + 190*scale_x
        end = x0 + 100*scale_x
        length = end - start
        n = 4
        for i in range(n):
            p1 = (x0 + 100*scale_x, y0)
            p2 = (start + (length / n) * i, y0 + 40*scale_y)
            p3 = (start + (length / n) * (i + 1), y0 + 40*scale_y)
            obj = polygon([p1, p2, p3])
            self.objects.append(obj)


background = Background()
sun = Sun()
clouds = Clouds()
ship1 = Ship(480, 200, 1, 1)
ship2 = Ship(290, 190, .5, .5)
umbrella1 = Umbrella(10, 240)
umbrella2 = Umbrella(220, 300, 0.33, 0.6)

def paint():
    global sun
    global background

    # background
    background.paint_background()

    # sun
    penColor("yellow")
    brushColor("yellow")
    sun.paint_sun()

    # cloud
    clouds.paint_clouds()

    # ships
    ship1.paint_ship()
    ship2.paint_ship()

    # umbrella
    umbrella1.paint_umbrella()
    umbrella2.paint_umbrella()

timer = onTimer(paint, 30)

# runLoopFunc(call_back)

run()