import random


def generate_secret_number():
    digits = list("0123456789")
    random.shuffle(digits)

    while digits[0] == '0':
        random.shuffle(digits)

    return ''.join(digits[:4])


def cows_and_bulls():
    secret = generate_secret_number()
    attempts = 10

    print("Компютърът намисли 4-цифрено число с различни цифри.")
    print("Опитай се да го познаеш. Имаш 10 опита!")

    for i in range(1, attempts + 1):
        guess = input(f"Опит {i}: ")
        if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
            print("Въведи валидно 4-цифрено число с различни цифри.")
            continue

        bulls = sum(1 for a, b in zip(secret, guess) if a == b)
        cows = sum(1 for digit in guess if digit in secret) - bulls

        if bulls == 4:
            print(f"Поздравления! Позна числото {secret} на {i}-ия опит!")
            return
        else:
            print(f"{bulls} бика, {cows} крави")

    print(f"Съжалявам, не успя. Числото беше {secret}.")


cows_and_bulls()
