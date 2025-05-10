import matplotlib.pyplot as plt


def plot_csv_data():
    try:
        with open("math_data.csv", "r", encoding="utf-8") as file:
            lines = file.readlines()

        x_values = []
        y_values = []

        for line in lines:
            line = line.replace("\n", "")
            parts = line.split(",")
            if len(parts) == 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    x_values.append(x)
                    y_values.append(y)
                except ValueError:
                    print(f"Невалидни числа в реда: {line}")

        plt.plot(x_values, y_values, color='green', marker='o')
        plt.title("Графика на функция от CSV файл")
        plt.xlabel("Аргументи (x)")
        plt.ylabel("Стойности (y)")
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print("Файлът math_data.csv не беше намерен.")


plot_csv_data()
