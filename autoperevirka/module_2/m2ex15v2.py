operand = None
operator = None
result = 0
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b, 
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else (print("Devision by Zero"), exit())
}


def calculation(op, a, b):
    operation = operations.get(op)
    if operation:
        return operation(a, b)
    return b


def input_num():
    while True:
        try:
            num = float(input("Enter your number: "))
            return num
        except ValueError:
            print("It's not a valid number. Try again.")


def input_op():
    while True:
        op = input("Enter operator: ")
        if op in operations or op == "=":
            return op
        else: 
            print("It's not '+'  '-'  '*'  '/'  or  '='. Try again.")


while operator != "=":
    operand = input_num()
    result = calculation(operator, result, operand)
    operator = input_op()

print("Answer: ", result)
