import turtle

turtle.setup(1000, 1000)

def fibonacci(n):
    if n in (1, 2):
        return 1
    if not n:
        return 0
    return fibonacci(n - 2) + fibonacci(n - 1)


t = turtle.Turtle()

for i in range(16):
    f = fibonacci(i)
    for i in range(4):
        t.fd(f)
        t.lt(90)
    t.circle(f, 90)

turtle.mainloop()
