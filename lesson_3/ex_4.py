numbers = []

while True:
    value = input("Въведете число; или 's' за край: ")
    if value == 's':
        break
    try:
        number = float(value)
        numbers.append(number)
    except ValueError:
        continue

if numbers:
    average = sum(numbers) / len(numbers)
    print("Средно аритметично:", average)
else:
    print("Няма въведени валидни числа.")
