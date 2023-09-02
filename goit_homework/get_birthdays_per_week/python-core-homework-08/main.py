from datetime import date, datetime
from collections import defaultdict


def get_week_day_name(birthday):
    week_day_names = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Monday",
        6: "Monday"
    }
    return week_day_names[birthday.weekday()]


def get_birthdays_per_week(users_list):
    today = date.today()
    birthdays_next_week = defaultdict(list)

    for user in users_list:
        birthday = user["birthday"].replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        days_to_birthday = (birthday - today).days

        if 0 <= days_to_birthday <= 6:
            birthdays_next_week[get_week_day_name(birthday)].append(user["name"])

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
