numbers = []

while True:
    value = input("Въведете число; или 's' за край: ")
    if value == 's':
        break
    try:
        num = float(value)
        numbers.append(num ** 2)
    except ValueError:
        continue

print("Сума на квадратите:", sum(numbers))
