# У компанії є кілька відділів. Список працівників для кожного відділу має такий вигляд:

# ['Robert Stivenson,28', 'Alex Denver,30']
# Це список рядків із прізвищем та віком співробітника, розділеними комами.

# Реалізуйте функцію запису даних про співробітників у файл, щоб інформація про кожного
# співробітника починалася з нового рядка.

# Функція запису в файл write_employees_to_file(employee_list, path), де:

# path – шлях до файлу.
# employee_list - список зі списками співробітників по кожному відділу, як у прикладі нижче:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Вимоги:

# запишіть вміст employee_list у файл, використовуючи режим "w".
# ми поки що не використовуємо менеджер контексту with
# кожен співробітник повинен бути записаний з нового рядка — тобто для попереднього списку
# вміст файлу має бути наступним:

#     Robert Stivenson,28
#     Alex Denver,30
#     Drake Mikelsson,19


# def write_employees_to_file(employee_list, path):

#     employee_list_without_dep = []

#     for department in employee_list:
#         for employee_data in department:
#             employee_list_without_dep.append(str(employee_data)) #  створюємо список без поділу на департаменти
            
    
#     text_to_write_in_file = '\n'.join(employee_list_without_dep) + '\n'  #  обʼднуєм список в рядок, розділяючу співробітників "\n"
    
#     file = open(path, 'w')
#     file.write(text_to_write_in_file)
#     file.close()

def write_employees_to_file(employee_list, path):

    text_to_write_in_file = ''

    for department in employee_list:
        for employee_data in department:
            text_to_write_in_file += str(employee_data) + '\n' 
            
    file = open(path, 'w')
    file.write(text_to_write_in_file)
    file.close()

employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
path = '/Users/sp/Docs/Projects/autoperevirka/Module 6/test.txt'
write_employees_to_file(employee_list, path)
