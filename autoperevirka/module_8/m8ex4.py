from random import randrange


def get_numbers_ticket(min, max, quantity):
    answ = []
    tickets = set()

    if min < 1 or max > 1000 or max < quantity or quantity < min:
        return answ

    while len(tickets) < quantity:
        tickets.add(randrange(min, max))

    answ = sorted(list(tickets))
     
    return answ



print(get_numbers_ticket(5, 100, 1000))
       