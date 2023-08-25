# Повернемося до нашого завдання із телефонними номерами. Компанія розширюється та вийшла на ринок Азії. 
# Тепер у списку можуть знаходитись телефони різних країн. Кожна країна має свій телефонний код .

# Компанія працює з наступними країнами

# Країна	Код ISO	Префікс
# Japan	JP	+81
# Singapore	SG	+65
# Taiwan	TW	+886
# Ukraine	UA	+380
# Щоб ми могли коректно виконати рекламну SMS кампанію, необхідно створити для кожної країни свій список телефонних номерів.

# Напишіть функцію get_phone_numbers_for_сountries, яка буде:

# Приймати список телефонних номерів.
# Санітизувати (нормалізувати) отриманий список телефонів клієнтів за допомогою нашої функції sanitize_phone_number.
# Сортувати телефонні номери за вказаними у таблиці країнами.
# Повертати словник зі списками телефонних номерів для кожної країни у такому вигляді:
# {
#     "UA": [<тут список телефонів>],
#     "JP": [<тут список телефонів>],
#     "TW": [<тут список телефонів>],
#     "SG": [<тут список телефонів>]
# }
# Якщо не вдалося порівняти код телефону з відомими, цей телефон повинен бути доданий до списку словника з ключем 'UA'.

def sanitize_phone_number(phone):
    rslt = phone
    for item in phone:
        if not item.isdigit():
            rslt = rslt.replace(item, "")
    return rslt


def get_phone_numbers_for_countries(list_phones):
    cleared_sorted_dict = {
        "UA": [],
        "JP": [],
        "TW": [],
        "SG": []
    }
    cleared_list = []

    for i in list_phones:
        cleared_list.append(sanitize_phone_number(i))

    for i in cleared_list: # сортування за країною
        if i.startswith("65"):
            cleared_sorted_dict["SG"].append(i)
        elif i.startswith("81"):
            cleared_sorted_dict["JP"].append(i)
        elif i.startswith("886"):
            cleared_sorted_dict["TW"].append(i)
        else:
            cleared_sorted_dict["UA"].append(i)

    return cleared_sorted_dict


print(get_phone_numbers_for_countries(["+886 943sdf2", "652(304)0", "++380000hi (3)"]))