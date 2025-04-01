from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant > 0:
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    print("Уравнението има 2 реални корена:")
    print(x1)
    print(x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print("Уравнението има един реален корен:")
    print(x)
else:
    x1 = complex(-b, sqrt(-discriminant)) / (2 * a)
    x2 = complex(-b, -sqrt(-discriminant)) / (2 * a)
    print("Уравнението има два комплексни корена:")
    print(x1)
    print(x2)
