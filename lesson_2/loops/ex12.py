x = int(input())

if x <= 0:
    print("Числото трябва да е положително.")
else:
    print("Числата, чиито квадрати са по-малки от", x, "са:")
    i = 1
    while i ** 2 < x:
        print(i, end=" ")
        i += 1
    print()  # нов ред
