num = int(input())

if 1 <= num <= 9:
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
else:
    print("Невалидно число.")
