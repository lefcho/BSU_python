numbers = []

while True:
    value = input("Въведете число; 's' за край: ")
    if value == 's':
        break
    try:
        number = float(value)
        numbers.append(number)
    except ValueError:
        continue

print("Въведени числа:", numbers)
print("Брой елементи:", len(numbers))
