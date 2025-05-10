from datetime import datetime, timedelta


def time_until_midnight():
    try:
        hour = int(input("Въведете час (0-23): "))
        minute = int(input("Въведете минути (0-59): "))

        now = timedelta(hours=hour, minutes=minute)
        midnight = timedelta(days=1)
        remaining = midnight - now

        hours_left = remaining.seconds // 3600
        minutes_left = (remaining.seconds % 3600) // 60

        print(f"До полунощ остават: {hours_left} часа и {minutes_left} минути.")

    except ValueError:
        print("Грешка.")


time_until_midnight()
