num = int(input())

if num > 0:
    if num % 2 == 0 and num % 3 == 0 and num % 7 == 0:
        print(f"Числото {num} се дели на 2, 3 и 7.")
    else:
        print(f"Числото {num} не се дели едновременно на 2, 3 и 7.")
else:
    print("Моля въведете положително цяло число.")
