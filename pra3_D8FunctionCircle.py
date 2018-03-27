import math

def circle(radius, area = False):
    circle_area = math.pi * radius ** 2
    circle_circum = math.pi * radius * 2

    if area == True:
        return circle_area
    else:
        return circle_circum

r = 3
print(circle(r))
print(circle(r, True))