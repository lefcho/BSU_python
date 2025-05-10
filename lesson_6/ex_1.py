from datetime import date


def days_since_start_of_year():
    try:
        day = int(input("Въведете ден: "))
        month = int(input("Въведете месец: "))
        year = date.today().year

        given_date = date(year, month, day)
        start_of_year = date(year, 1, 1)

        diff = (given_date - start_of_year).days
        print(f"Минали са {diff} дни от началото на годината.")

    except ValueError:
        print("Error")


days_since_start_of_year()
