numbers = []

while True:
    value = input("Въведете число; или 's' за край: ")
    if value == 's':
        break
    try:
        num = float(value)
        if num >= 0:
            numbers.append(num)
    except ValueError:
        continue

print(numbers[::-1])
