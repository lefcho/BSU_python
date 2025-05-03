def calc_price(days, beds, ticket):
    bed_price = 50
    total = bed_price * beds * days + 2 * ticket
    return total


print("Total price", calc_price(5, 2, 120))
