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

even_index_numbers = numbers[::2]
print("Числа на четни индекси в обратен ред:", even_index_numbers[::-1])
