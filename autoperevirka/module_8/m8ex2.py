"""
Напишіть функцію визначення кількості днів у конкретному місяці. Ваша функція повинна приймати 
два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік, 
що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.
"""

# from datetime import datetime


# def get_days_in_month(month, year):
#     days_in_month = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
#     if month == 12:
#         month = 1
#         year += 1
#     else:
#         month += 1
#     days_in_month1 = datetime.strptime(f"{year}-{month}-01", "%Y-%m-%d")
#     return (days_in_month1 - days_in_month).days
        
from datetime import date


def get_days_in_month(month, year):
    days_in_month = date(year, month, 1)
    
    
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    days_in_month1 = date(year, month, 1)
    return (days_in_month1 - days_in_month).days

print(get_days_in_month(2, 1996))