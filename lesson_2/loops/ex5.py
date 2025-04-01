start = int(input("a: "))
end = int(input("b: "))

if start >= end:
    print("Първото число трябва да е по-малко от второто.")
else:
    product = 1

    for i in range(start, end + 1):
        if i % 2 != 0:
            product *= i

    if product != 1:
        print(product)
    else:
        print("В интервала няма нечетни числа.")
