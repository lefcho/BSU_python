def calc_price(pizza_price, pizza_amount, drink_price, drinks_amount):
    delivery_fee = 5

    if pizza_price < 0 or pizza_amount < 0 or drink_price < 0 or drinks_amount < 0:
        print("Negative numbers!")
        return

    total = pizza_price * pizza_amount + drink_price * drinks_amount + delivery_fee
    print(f"Sum: {total:.2f} lv.")


calc_price(12.5, 2, 2.0, 3)
