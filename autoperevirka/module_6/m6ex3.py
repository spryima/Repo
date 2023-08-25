# У попередній задачі ми записали співробітників у файл у такому вигляді:

# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19
# Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path), 
# яка читатиме дані з файлу та повертатиме список співробітників у вигляді:

# ['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
# Пам'ятайте про наявність символу кінця рядка \n під час читання даних із файлу. Його 
# необхідно прибирати при додаванні прочитаного рядка до списку.

# Вимоги:

# прочитайте вміст файлу за допомогою режиму "r".
# ми поки що не використовуємо менеджер контексту with
# поверніть із функції список співробітників із файлу


def read_employees_from_file(path):
    file = open(path, 'r')
    employees_list = file.readlines()
    file.close()
    
    for i in range(len(employees_list)):
        if employees_list[i][-1:] == '\n':
            employees_list[i] = employees_list[i][:-1]
#           employees_list[i] = employees_list[i].replace('\n', '')
    return employees_list


# Один з файлів який дається на перевірку записаний не функцією із завдання 2 і не має в кінці строки ʼ\nʼ

path = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
print(read_employees_from_file(path))


