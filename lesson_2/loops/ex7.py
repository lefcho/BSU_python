n = int(input())

if n < 1:
    print("n трябва да бъде поне 1.")
else:
    suma = 0
    for i in range(1, n + 1):
        suma += i**2
    print(suma)
