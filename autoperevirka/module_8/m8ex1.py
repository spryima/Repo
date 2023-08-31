"""
Розробіть функцію get_days_from_today(date), яка повертатиме кількість днів від поточної 
дати, де параметр date - це рядок формату '2020-10-09' (рік-місяць-день).
"""

from datetime import datetime


def get_days_from_today(date):
    check_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.now()
    if today > check_date:
        delta_days = (today - check_date).days
    else:
        delta_days = (check_date - today).days
 
    return delta_days



print(get_days_from_today("2025-10-09"))
