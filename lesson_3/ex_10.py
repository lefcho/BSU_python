numbers = []

while True:
    value = input("Въведете число; или 's' за край: ")
    if value == 's':
        break
    try:
        num = float(value)
        numbers.append(num)
    except ValueError:
        continue

sum_even = sum(numbers[i] for i in range(0, len(numbers), 2))

product_odd = 1
for i in range(1, len(numbers), 2):
    product_odd *= numbers[i]

print("Сума на четни индекси:", sum_even)
print("Произведение на нечетни индекси:", product_odd)
