def reverse_file_lines():
    try:
        with open("string_data.txt", "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        reversed_lines = lines[::-1]

        with open("string_reverse.txt", "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(reversed_lines))

        print("Saved in string_reverse.txt.")
    except FileNotFoundError:
        print("string_data.txt not found.")


reverse_file_lines()
