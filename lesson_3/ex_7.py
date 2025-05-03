numbers = []

while True:
    value = input("Въведете число; или 's' за край: ")
    if value == 's':
        break
    try:
        num = int(value)
        numbers.append(num)
    except ValueError:
        continue

limit = int(input("Въведете лимит: "))

print("Валидни двойки със сума ≤", limit, ":")
for i in range(len(numbers) - 1):
    if numbers[i] + numbers[i+1] <= limit:
        print(numbers[i], numbers[i+1])
