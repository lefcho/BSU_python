n = int(input())

if n >= -1:
    print("Грешка: Числото трябва да е по-малко от -1.")
else:
    count = 0
    for i in range(n, -1 + 1):
        if i % 7 == 0:
            count += 1
    print("Броят на числата в интервала от", n, "до -1, които се делят на 7, е:", count)
