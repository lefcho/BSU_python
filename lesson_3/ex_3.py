even_numbers = []
odd_numbers = []

while True:
    value = input("Въведете число; 's' за край: ")
    if value == 's':
        break
    try:
        number = int(value)
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    except ValueError:
        continue

print("Четни числа:", even_numbers, "Брой:", len(even_numbers))
print("Нечетни числа:", odd_numbers, "Брой:", len(odd_numbers))
