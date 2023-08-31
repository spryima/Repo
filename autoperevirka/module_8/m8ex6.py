from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    for _ in range(len(number_list)):
        number_list[_] = Decimal(str(number_list[_]))

    return sum(number_list)/Decimal(str(len(number_list)))
