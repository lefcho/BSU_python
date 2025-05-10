def split_mixed_data():
    try:
        with open("mixed_data.txt", "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        numbers = []
        names = []

        for line in lines:
            parts = line.strip().split()

            numbers.append(parts[0])
            names.append(parts[1])

        with open("numbers.txt", "w", encoding="utf-8") as num_file:
            num_file.write("\n".join(numbers))

        with open("names.txt", "w", encoding="utf-8") as name_file:
            name_file.write("\n".join(names))

        print("Done.")
    except FileNotFoundError:
        print("Error")

split_mixed_data()