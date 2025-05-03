matrix = []
current_index = 0
matrix.append([])

while True:
    value = input("Въведете число; или 's' за край: ")
    if value == 's':
        break
    try:
        num = int(value)
        matrix[current_index].append(num)

        if len(matrix[current_index]) > current_index:
            current_index += 1
            matrix.append([])

    except ValueError:
        continue

for row in matrix:
    if row:
        print(row)
