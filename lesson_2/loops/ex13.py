n = int(input())

if n < 3:
    print("Няма поредица от последователни числа, чиито двойни сборове са <= ", n)
else:
    max_i = (n - 1) // 2

    print("Поредицата от числа е:")
    for num in range(1, max_i + 2):
        print(num, end=" " )
    print()
