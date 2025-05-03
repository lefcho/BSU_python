def area(a, h):
    if a <= 0 or h <= 0:
        return -1
    return (a * h) / 2


print(area(5, 10))
print(area(-3, 4))
print(area(0, 7))
