n = int(input())

if n <= 10:
    print("Числото трябва да е по-голямо от 10.")
else:
    a = 1
    for i in range(10, n + 1):
        a *= i
    print(f"Произведението е: {a}")
