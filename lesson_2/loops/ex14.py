rows = int(input())

if rows < 1:
    print("Броят на редовете трябва да е поне 1.")
else:
    for i in range(1, rows + 1):
        if i == 1:
            print("о")
        elif i == rows:
            print("о" * rows)
        else:

            print("о" + " " * (i - 2) + "о")
