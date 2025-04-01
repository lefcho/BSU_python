n = int(input())

if n < 1:
    print("n трябва да бъде поне 1")
else:
    product = 1.0
    for i in range(1, n + 1):
        product *= (i - 1) / (i + 1)

    print(f"Product: {product}")
