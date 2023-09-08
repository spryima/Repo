def generator_numbers(string=""):
    number = []
    label = False
    for i in string:

        if i.isdigit():
            number.append(i)
            label = True

        if i.isdigit() == False and label == True:
            label = False
            yield "".join(number)
            number = []

def sum_profit(string):
    result = 0
    for num in generator_numbers(string):
        result += int(num)
    return result
    

s = "The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."
print(sum_profit(s))