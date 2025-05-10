import random


def guess_the_number():
    secret = random.randint(0, 100)
    attempts = 10

    print("Опитай се да познаеш ! Имаш 10 опита.")

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Опит {i}: "))
        except ValueError:
            print("Моля, въведи цяло число.")
            continue

        if guess < secret:
            print("Намисленото число е по-голямо.")
        elif guess > secret:
            print("Намисленото число е по-малко.")
        else:
            print(f"Поздравления! Позна числото {secret} на {i}-ия опит!")
            return

    print(f"Не позна. Числото беше {secret}.")


guess_the_number()
