# https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python

# Johnny is a farmer and he annually holds a beet farmers convention "Drop the beet".

# Every year he takes photos of farmers handshaking. Johnny knows that no 
# two farmers handshake more than once. He also knows that someof the possible 
# handshake combinations may not happen.

# However, Johnny would like to know the minimal amount of people that participated 
# this year just by counting all the handshakes.

# Help Johnny by writing a function, that takes the amount of handshakes and returns 
# the minimal amount of people needed to perform these handshakes (a pair of farmers 
# handshake only once).

def get_participants(handshakes):    
    if handshakes == 0:
        return 0
    lst = [0 for x in range(handshakes + 5)]
    for x in range(handshakes + 5):
        lst[x] = lst[x-1] + x 
    for x in range(handshakes + 5):
        if handshakes <= lst[x]:
            return x + 1



print(get_participants(1))
    