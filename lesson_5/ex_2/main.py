def double_integers():
    try:
        with open("int_data.txt", "r", encoding="utf-8") as infile:
            lines = infile.readlines()

        doubled_lines = []
        for line in lines:
            line = line.strip()
            if line.isdigit():
                doubled_lines.append(str(int(line) * 2))
            else:
                doubled_lines.append("Not an int")

        with open("doubled_ints.txt", "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(doubled_lines))

        print("Числата са записани в doubled_ints.txt.")
    except FileNotFoundError:
        print("Error")


double_integers()