from datetime import datetime, timedelta


def pizza_order():

    PIZZA_PRICE = 10.50
    COLA_PRICE = 2.00

    try:
        pizzas = int(input("Въведете брой пици: "))
        colas = int(input("Въведете брой коли: "))

        total_price = pizzas * PIZZA_PRICE + colas * COLA_PRICE
        order_time = datetime.now()
        delivery_time = order_time + timedelta(hours=2)

        print(f"Цена на поръчката: {total_price:.2f} лв.")
        print("Час на доставка:", delivery_time.strftime("%H:%M"))

    except ValueError:
        print("Грешка.")


pizza_order()
