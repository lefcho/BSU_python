import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(distance(0, 0, 3, 4))
print(distance(1, 2, 1, 2))
print(distance(-1, -1, 2, 3))
