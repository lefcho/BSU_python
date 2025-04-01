start = int(input("a: "))
end = int(input("b: "))

if start >= end:
    print("Първото число трябва да е по-малко от второто.")
else:
    suma = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            suma += i
    print(f"Sum: {suma}")
