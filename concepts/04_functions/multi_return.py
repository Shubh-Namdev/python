import math

def area_circumference(radius) :
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius

    return area, circumference

a, c = area_circumference(5)