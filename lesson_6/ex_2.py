from datetime import datetime


def date_difference():
    try:
        date1_str = input("Въведете първата дата (дд.мм.гггг): ")
        date2_str = input("Въведете втората дата (дд.мм.гггг): ")

        date1 = datetime.strptime(date1_str, "%d.%m.%Y")
        date2 = datetime.strptime(date2_str, "%d.%m.%Y")

        if date1 > date2:
            date1, date2 = date2, date1

        days_diff = (date2 - date1).days

        years = days_diff // 365
        days_diff %= 365
        months = days_diff // 30
        days = days_diff % 30

        print(f"Разлика: {years} години, {months} месеца, {days} дни")

    except ValueError:
        print("Грешка.")


date_difference()
