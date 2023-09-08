result = 0
operand = None
operator = None
wait_for_number = True


def calculation():  
    if operator == '+':
        return result + operand
    elif operator == '-':
        return result - operand
    elif operator == '*':
        return result * operand
    elif operator == '/':
        if operand == 0:
            print('Division by zero is not allowed')
            exit()
        return result / operand


while operator != "=":
    if wait_for_number:
        try:
            operand = float(input("Enter your number "))
            result = calculation()
        except ValueError:
            print(f"{operand} not a number. Try again")
            wait_for_number = True
            continue
        if operator is None:
            result = operand
        wait_for_number = False
    else: 
        operator = input('Enter operator ')
        if operator in ('+', '-', '*', '/'):
            wait_for_number = True
        elif operator == '=':
            break
        else:
            print(f"{operator} is not '+' or '-' or '/' or '*'. Try again")
            wait_for_number = False
            continue
print(result)