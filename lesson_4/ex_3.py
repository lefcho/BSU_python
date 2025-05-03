def print_employee(fname, lname, age, position):
    if age < 0:
        print("Age cannot be negative.")
        return
    print(f"Name: {fname} {lname}")
    print(f"Age: {age}")
    print(f"Position: {position}")


print_employee("Ivan", "Ivanov", 34, "Manager")
