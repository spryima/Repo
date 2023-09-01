from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):

    today = date(2023, 12, 26)    # Підставляємо кастомну дату замість today
    # today = date.today()



    birthdays_next_week = defaultdict(list)

    for user in users:
        birthday = user["birthday"].replace(year=today.year)
        
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        
        days_to_birthday = (birthday - today).days
        
        if 0 <= days_to_birthday < 7:
            week_day = date.strftime(birthday, "%A")
            if week_day in ("Sunday", "Saturday"):
                birthdays_next_week["Monday"].append(user["name"])
            else:
                birthdays_next_week[week_day].append(user["name"])

    
    return birthdays_next_week


today = date(2023, 12, 26)


users_list = [
    {"name": "John нема", "birthday": (today + timedelta(days=-5))},
    {"name": "Doe нема", "birthday": (today + timedelta(days=-6))},
    {"name": "Alice є в понеділок", "birthday": (datetime(2021, 1, 1)).date()},
    {"name": "Понеділок1", "birthday": (today + timedelta(days=5))},
    {"name": "Понеділок2", "birthday": (today + timedelta(days=6))},
    {"name": "Пʼятниця", "birthday": (today + timedelta(days=3))},


]


print(dict(get_birthdays_per_week(users_list)))

