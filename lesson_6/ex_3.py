from datetime import datetime, timedelta


def add_two_months():
    try:
        date_str = input("Въведете дата (дд.мм.гггг): ")
        original_date = datetime.strptime(date_str, "%d.%m.%Y")

        new_date = original_date + timedelta(days=60)
        print("Датата след 2 месеца е:", new_date.strftime("%d.%m.%Y"))

    except ValueError:
        print("Грешка.")


add_two_months()
