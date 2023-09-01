from collections import deque

MAX_LEN = 10 
fifo = deque([], 10)


def push(element):
    fifo.append(element)


def pop():
    return fifo.popleft()




for _ in range(20):
    push(_)

print(pop())
print(fifo)