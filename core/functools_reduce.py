from functools import reduce


def amount_payment(payment):
    return reduce(lambda x, y: x + y if x > 0 and y > 0 else x, payment)
