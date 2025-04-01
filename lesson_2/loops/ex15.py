n = int(input())

if n < 1:
    print("Броят трябва да е поне 1.")
elif n == 1:
    print("о")
else:

    print("о" * n)

    for i in range(n - 2):
        print("о" + " " * (n - 2) + "о")

    print("о" * n)
