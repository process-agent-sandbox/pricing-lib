def price(amount, discount=0.0, tax=0.25):
    return round(amount * (1 - discount) * (1 + tax), 2)
