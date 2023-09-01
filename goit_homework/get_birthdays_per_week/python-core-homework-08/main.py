from datetime import date, datetime
from collections import defaultdict


def get_birthdays_per_week(users_list):
    today = date.today()
    birthdays_next_week = defaultdict(list)

    for user in users_list:
        birthday = user["birthday"].replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_to_birthday = (birthday - today).days

        if 0 <= days_to_birthday < 7:
            week_day = birthday.weekday()
            if week_day == 0: 
                week_day = "Monday"
            if week_day == 1: 
                week_day = "Tuesday"
            if week_day == 2: 
                week_day = "Wednesday"
            if week_day == 3: 
                week_day = "Thursday"
            if week_day == 4: 
                week_day = "Friday"
            if week_day == 5: 
                week_day = "Saturday"
            if week_day == 6: 
                week_day = "Sunday"

            if week_day in ("Sunday", "Saturday"):
                birthdays_next_week["Monday"].append(user["name"])
            else:
                birthdays_next_week[week_day].append(user["name"])

    return birthdays_next_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
