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

try:
    m = int(input("Въведете m: "))
    n = int(input("Въведете n: "))
    sublist = numbers[m:n+1]
    print("Подлист:", sublist)

except (ValueError, IndexError):
    print("Невалидни индекси!")
