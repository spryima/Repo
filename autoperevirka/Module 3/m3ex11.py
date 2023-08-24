# Однією з класичних задач на розуміння рекурсії, яку часто задають на співбесідах, 
# особливо початківцям-програмістам — це ряд Фібоначчі.

# Ряд Фібоначчі — це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ... де кожне 
# наступне число послідовності виходить додаванням двох попередніх членів ряду.

# У загальному вигляді для обчислення n-го члена ряду Фібоначчі слід обчислити вираз:

# Fn = Fn-1 + Fn-2.

# Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа 
# послідовності доти, доки виклик не сягне членів ряду менше n = 1, на якій 
# задана послідовність.


# ____________________       Класичний варіант

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
    
# ____________________       варіант з Memoization

# ____________________       за допомогою алгоритму динамічного програмування

def fibonacci_dynamic(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


n = int(input("Введіть число n: "))
result = fibonacci_dynamic(n)
print(f"Число Фібоначчі для n = {n} дорівнює {result}")

