from collections import deque

MAX_LEN = 10
lifo = deque([], MAX_LEN)


def push(element):  
    deque.appendleft(lifo, element)


def pop():
    return deque.popleft(lifo)




for _ in range(20):
    push(_)

print(pop())
print(lifo)
