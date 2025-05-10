def reverse_file_lines():
    try:
        with open("string_data.txt", "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        reversed_lines = lines[::-1]

        with open("string_reverse.txt", "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(reversed_lines))

        print("Done")
    except FileNotFoundError:
        print("Error.")

reverse_file_lines()
